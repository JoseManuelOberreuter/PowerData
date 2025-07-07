# Use case for health check logic 
from app.domain.models.health_status import HealthStatus

class HealthCheckUseCase:
    """Simple use case for health check."""
    
    def execute(self) -> HealthStatus:
        """Execute health check and return status."""
        # Always return healthy
        return HealthStatus.healthy("Service is running normally")