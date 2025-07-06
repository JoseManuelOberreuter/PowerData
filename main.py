# Main entry point for the application

from fastapi import FastAPI
from app.infrastructure.api.health_router import router as health_router

app = FastAPI(prefix="/api")

app.include_router(health_router)

# Run the FastAPI application with uvicorn server on port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 