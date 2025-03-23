from fastapi import APIRouter, Query
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

# Initialize APIRouter
search_router = APIRouter()

# Load pre-trained SentenceTransformer model
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

# Function to load documents from a text file
def load_documents_from_txt(file_path: str):
    """
    Reads documents line by line from a text file.
    Each line is treated as a separate document.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        documents = f.readlines()
    return [doc.strip() for doc in documents if doc.strip()]  # Remove empty lines

# Load sample documents dynamically (choose one based on your dataset format)
documents = load_documents_from_txt("documents.txt")  # Example: Load from text file

# Generate embeddings for the loaded documents
embeddings = model.encode(documents)

# Set up FAISS indices for similarity search (L2 and Cosine similarity)
embedding_dim = embeddings.shape[1]

# L2 Distance Index (default)
index_l2 = faiss.IndexFlatL2(embedding_dim)
index_l2.add(np.array(embeddings))

# Cosine Similarity Index (normalize embeddings for inner product search)
index_cosine = faiss.IndexFlatIP(embedding_dim)
normalized_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
index_cosine.add(np.array(normalized_embeddings))

@search_router.get("/search")
def search(q: str, metric: str = Query("cosine", enum=["cosine", "l2"])):
    """
    Search for similar documents based on query and similarity metric.
    """
    # Generate embedding for the query
    query_embedding = model.encode([q])

    # Normalize query embedding for cosine similarity if selected
    if metric == "cosine":
        query_embedding = query_embedding / np.linalg.norm(query_embedding)

        # Perform similarity search using cosine similarity (inner product)
        distances, indices = index_cosine.search(np.array(query_embedding), k=5)

        # Convert distances to cosine similarity scores (inner product values)
        results = [
            {"document": documents[i], "score": float(distances[0][j])}
            for j, i in enumerate(indices[0])
        ]

    elif metric == "l2":
        # Perform similarity search using L2 distance
        distances, indices = index_l2.search(np.array(query_embedding), k=5)

        # Convert distances to scores (1 - normalized distance for better interpretation)
        results = [
            {"document": documents[i], "score": float(1 - distances[0][j])}
            for j, i in enumerate(indices[0])
        ]

    else:
        return {"error": "Invalid metric. Use 'cosine' or 'l2'."}

    return {"query": q, "metric": metric, "results": results}
