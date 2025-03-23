import faiss
import numpy as np
import os

class FI:
    def __init__(self, dimension, index_path=None):
        self.dimension = dimension
        self.index_path = index_path
        self.index = faiss.read_index(index_path) if index_path and os.path.exists(index_path) else faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        self.index.add(np.array(embeddings, dtype=np.float32))

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        return indices[0]

    def save_index(self, index_path):
        faiss.write_index(self.index, index_path)
