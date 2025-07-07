# Model for health status data 
from datetime import datetime

class HealthStatus:
    """Simple health status model."""
    
    def __init__(self, status: str, message: str = None):
        # Initialize health status with current timestamp
        self.status = status
        self.timestamp = datetime.now()
        self.message = message
    
    def is_healthy(self) -> bool:
        # Check if service is healthy
        return self.status == "healthy"
    
    def to_dict(self) -> dict:
        # Convert to dictionary for API response
        return {
            "status": self.status,
            "timestamp": self.timestamp.isoformat(),
            "message": self.message
        }
    
    @classmethod
    def healthy(cls, message: str = "Service is running"):
        # Factory method to create healthy status
        return cls("healthy", message)
    
    @classmethod 
    def unhealthy(cls, message: str = "Service has issues"):
        # Factory method to create unhealthy status
        return cls("unhealthy", message)