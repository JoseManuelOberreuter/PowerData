# Main entry point for the application

from fastapi import FastAPI
from app.infrastructure.api.health_router import router as health_router

app = FastAPI(
    title="health-check-service",
    description="Simple API for service health monitoring",
    version="1.0.0",
    docs_url="/docs",  
    redoc_url="/redoc" 
)

app.include_router(health_router, prefix="/api")

# Run the FastAPI application with uvicorn server on port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 