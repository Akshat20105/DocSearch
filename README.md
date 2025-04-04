# **DocSearch**

## **Overview**
This project uses **FastAPI** (backend) to create a web application that finds similar documents using embeddings and vector search techniques. The backend uses **Hugging Face Sentence Transformers** to generate embeddings and **FAISS** for efficient similarity search.

---

## **Features**
- **Backend (FastAPI)**:
  - Provides API endpoints for document similarity search.
  - Uses Hugging Face Sentence Transformers for embedding generation.
  - Stores embeddings in FAISS for fast vector search.
---

## **Project Structure**
```
project/
├── .venv/         # Virtual environment (auto-managed)
├── backend/       # FastAPI backend
│   ├── main.py    # FastAPI entry point
│   ├── embeddings.py
│   ├── api.py # API routes
│   ├── routes.py # API routes
|
├── requirements.txt # List of dependencies
└── README.md      # Project documentation
```

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/Akshat20105/DocSearch
cd DocSearch
```

### **Step 2: Create a Virtual Environment**
Create and activate a virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate   # On Windows
```

### **Step 3: Install Dependencies**
Install all required Python libraries:
```sh
pip install -r requirements.txt
```

### **Step 4: Run the Backend (FastAPI)**
Start the FastAPI server:
```sh
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
The backend will be available at `http://localhost:8000`.
---

## **Usage**

### Access the Web Application:
1. Open your browser and navigate to `http://localhost:5000`.
2. Interact with the UI to fetch similar documents based on your query.

### Test the API Directly:
You can test the FastAPI endpoint using tools like `curl` or Postman:
```sh
curl "http://localhost:8000/api/data"
```

---

## **Technologies Used**
- **Backend**: FastAPI, Hugging Face Sentence Transformers, FAISS.
- **Vector Search**: FAISS for efficient similarity search.
- **Embedding Models**: Hugging Face's `multi-qa-MiniLM-L6-cos-v1`.

---

## **Future Enhancements**
- Add real-time indexing for new documents.
- Enhance UI with advanced filtering options.
- Deploy the application on cloud platforms like AWS or Azure.

---
