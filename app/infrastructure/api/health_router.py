# API routes for health check service 
from fastapi import APIRouter
from app.domain.use_cases.health_check_usecase import HealthCheckUseCase

router = APIRouter()

# Health check endpoint that returns healthy status
@router.get(
    "/health",
    summary="Health Check",
    description="Verifica el estado de salud del servicio",
    response_description="Estado actual del servicio"
)
async def health_check():
    """
    Endpoint para verificar el estado de salud del servicio.
    """
    use_case = HealthCheckUseCase()
    health_status = use_case.execute()
    return health_status.to_dict()