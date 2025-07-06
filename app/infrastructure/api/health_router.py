# API routes for health check service 
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")  
async def health_check():
    return {"status": "healthy"} 