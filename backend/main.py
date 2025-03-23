from fastapi import FastAPI
from api import search_router  # Import the router from api.py

# Initialize FastAPI app
app = FastAPI()

# Include the router from api.py
app.include_router(search_router, prefix="/api", tags=["Search"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
