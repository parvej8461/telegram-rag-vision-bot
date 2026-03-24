import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(doc_dir="data/docs"):
    docs = []
    for file in os.listdir(doc_dir):
        if file.endswith((".txt", ".md")):
            with open(os.path.join(doc_dir, file), "r", encoding="utf-8") as f:
                docs.append({"content": f.read(), "source": file})
    return docs

def chunk_documents(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = []
    for doc in docs:
        for i, chunk in enumerate(splitter.split_text(doc["content"])):
            chunks.append({
                "text": chunk,
                "source": doc["source"],
                "chunk_id": i
            })
    return chunks