# API routes for health check service 
from fastapi import APIRouter

router = APIRouter()

# Health check endpoint that returns healthy status
@router.get("/health")  
async def health_check():
    return {"status": "healthy"} 