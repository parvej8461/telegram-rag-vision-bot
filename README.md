&#x20;Telegram RAG + Vision Bot
## snippet of my telegram bot 
<img width="1104" height="929" alt="image" src="https://github.com/user-attachments/assets/68a3908b-a93d-4688-bc17-11d1a5507cfa" />


A lightweight multimodal AI assistant built using:



Retrieval-Augmented Generation (RAG)

Local LLM via Ollama

Image captioning (BLIP)



Runs fully offline with minimal resources.



&#x20;Features

/ask <query> → Answers from local knowledge base (RAG)

Image upload → Generates caption + keywords

Local embeddings + vector search (ChromaDB)



No paid APIs

&#x20;System Design

User → Telegram Bot

&#x20;       ↓

&#x20;  Command Router

&#x20;       ↓

&#x20;┌───────────────┬───────────────┐

&#x20;│ RAG Pipeline  │ Vision Model  │

&#x20;│               │               │

&#x20;│ Docs → Embed  │ Image → BLIP  │

&#x20;│ → ChromaDB    │ → Caption     │

&#x20;│ → Retrieve    │               │

&#x20;│ → LLM         │               │

&#x20;└───────────────┴───────────────┘



&#x20;Tech Stack

Component	Tool

Bot	python-telegram-bot

Embeddings	all-MiniLM-L6-v2

Vector DB	ChromaDB

LLM	Ollama (tinyllama)

Vision	BLIP (HuggingFace)



&#x20;Setup

1\. Clone repo

git clone <your-repo>

cd telegram-rag-vision-bot

2\. Create environment

python -m venv venv

venv\\Scripts\\activate

3\. Install dependencies

pip install -r requirements.txt

4\. Setup environment



Create .env:



TELEGRAM\_BOT\_TOKEN=token

OLLAMA\_URL=http://localhost:11434

OLLAMA\_MODEL=tinyllama



5\. Run Ollama

ollama pull tinyllama

ollama serve

6\. Add documents



Place .txt or .md files in:



data/docs/

7\. Index data (one-time)



Uncomment in main.py:



docs = load\_documents()

chunks = chunk\_documents(docs)

vector\_store.add\_chunks(chunks)



Run:



python main.py



Then comment it back.



8\. Run bot

python main.py

Usage

/ask What is the return policy?

Send image → get caption

Evaluation Criteria Mapping

Code Quality

Modular: rag/, vision/

Clear separation of concerns

System Design

Clean pipeline: retrieval → generation

Decoupled vision + text

Model Use

Local LLM (cost-efficient)

Lightweight embeddings

Efficiency

Persistent ChromaDB

TinyLlama for low RAM systems

User Experience

Fast responses

Simple commands

Innovation

Multimodal (text + image)

Fully offline AI assistant

