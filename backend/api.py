from fastapi import FastAPI, UploadFile, File
import os
from backend.routes import FI
from embeddings import generate_embedding, load_documents

DATA_FOLDER = "data/"
INDEX_PATH = "index/vector_index.faiss"

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs("index/", exist_ok=True)

app = FastAPI()

documents = load_documents(DATA_FOLDER)
document_embeddings = [generate_embedding(doc) for doc in documents] if documents else []

embedding_dim = len(document_embeddings[0]) if document_embeddings else 384
faiss_index = FI(dimension=embedding_dim, index_path=INDEX_PATH)

if document_embeddings:
    faiss_index.add_embeddings(document_embeddings)
    faiss_index.save_index(INDEX_PATH)

@app.get("/")
def home():
    return {"message": "Welcome to the DocSearch API"}

@app.post("/api/add_document/")
async def add_document(file: UploadFile = File(...)):
    file_path = os.path.join(DATA_FOLDER, file.filename)

    content = await file.read()
    text = content.decode("utf-8").strip()

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    new_embedding = generate_embedding(text)
    documents.append(text)
    faiss_index.add_embeddings([new_embedding])
