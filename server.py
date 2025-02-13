from fastapi import FastAPI
from api.routes import books  # Import the books router

app = FastAPI()

# Include the books router with the /api/v1 prefix
app.include_router(books.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """A simple health check endpoint."""
    return {"status": "OK"}