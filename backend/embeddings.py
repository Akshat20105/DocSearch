from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    return model.encode(text).tolist()

def load_documents(data_folder):
    return [open(os.path.join(data_folder, file), "r", encoding="utf-8").read().strip() for file in os.listdir(data_folder)]
