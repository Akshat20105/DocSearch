from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load pre-trained model and FAISS index
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
index = faiss.read_index("faiss_index.bin")

# Sample documents (used to map results back to text)
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is transforming the world.",
    "Python is a popular programming language.",
    "Space exploration is fascinating.",
    "The stock market fluctuates daily."
]

@app.get("/api/search")
def search(q: str):
    """
    Search for similar documents based on query.
    """
    # Generate embedding for the query
    query_embedding = model.encode([q])

    # Perform similarity search in FAISS
    k = 5  # Number of top results to return
    distances, indices = index.search(np.array(query_embedding), k)

    # Retrieve the top-k documents and their scores
    results = [{"document": documents[i], "score": float(1 - distances[0][j])} 
               for j, i in enumerate(indices[0])]

    return {"query": q, "results": results}
