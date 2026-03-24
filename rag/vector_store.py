import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, persist_dir="data/chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection("rag_docs")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')

    def add_chunks(self, chunks):
        ids = [f"{c['source']}_{c['chunk_id']}" for c in chunks]
        texts = [c["text"] for c in chunks]
        embeddings = self.embedder.encode(texts).tolist()

        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=texts
        )

    def query(self, query_text, top_k=3):
        emb = self.embedder.encode([query_text]).tolist()
        return self.collection.query(query_embeddings=emb, n_results=top_k)