from vision.captioner import ImageCaptioner
from rag.loader import load_documents, chunk_documents
from rag.vector_store import VectorStore
from rag.llm import ask_llm
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters
# Load environment variables
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
vector_store = VectorStore()

captioner = ImageCaptioner()

def rag_answer(query):
    results = vector_store.query(query)

    if not results or not results.get("documents") or not results["documents"][0]:
        return " I couldn't find relevant information."

    docs = results['documents'][0]
    context = "\n".join(docs)

    prompt = f"""
Answer using the context below:

{context}

Question: {query}
Answer:
"""
    return ask_llm(prompt)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" Bot is working! Send /help")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start\n/help")


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Use: /ask your question")
        return

    answer = rag_answer(query)
    await update.message.reply_text(answer)

async def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        await update.message.reply_text("Send an image with caption /image")
        return

    photo = update.message.photo[-1]
    file = await photo.get_file()

    import os
    os.makedirs("downloads", exist_ok=True)

    file_path = f"downloads/{photo.file_id}.jpg"
    await file.download_to_drive(file_path)

    caption, keywords = captioner.caption(file_path)

    response = f"📷 {caption}\n {', '.join(keywords)}"
    await update.message.reply_text(response)



def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(MessageHandler(filters.PHOTO, image_handler))

   

    print(" Bot is running...")
    app.run_polling()


if __name__ == "__main__":


    main()