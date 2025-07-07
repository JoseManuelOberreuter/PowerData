# API routes for health check service 
from fastapi import APIRouter
from app.domain.use_cases.health_check_usecase import HealthCheckUseCase

router = APIRouter()

# Health check endpoint that returns healthy status
@router.get("/health")  
async def health_check():
    use_case = HealthCheckUseCase()
    health_status = use_case.execute()
    return health_status.to_dict()