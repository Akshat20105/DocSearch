from fastapi import FastAPI
from .api import search_router  # Import routes from api.py

# Initialize FastAPI app
app = FastAPI()

# Include routes from api.py
app.include_router(search_router, prefix="/api", tags=["Search"])
