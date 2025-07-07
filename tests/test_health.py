# Tests for the health check service 
import pytest
from app.domain.use_cases.health_check_usecase import HealthCheckUseCase
from app.domain.models.health_status import HealthStatus

def test_health_check_use_case():
    """Test health check use case returns healthy status."""
    use_case = HealthCheckUseCase()
    result = use_case.execute()
    
    assert isinstance(result, HealthStatus)
    assert result.is_healthy() == True
    assert result.status == "healthy"

def test_health_status_healthy():
    """Test healthy status creation."""
    status = HealthStatus.healthy("Service running")
    
    assert status.is_healthy() == True
    assert status.status == "healthy"
    assert status.message == "Service running"

def test_health_status_unhealthy():
    """Test unhealthy status creation."""
    status = HealthStatus.unhealthy("Service down")
    
    assert status.is_healthy() == False
    assert status.status == "unhealthy"
    assert status.message == "Service down"

def test_health_status_to_dict():
    """Test converting status to dictionary."""
    status = HealthStatus.healthy("Test message")
    result_dict = status.to_dict()
    
    assert result_dict["status"] == "healthy"
    assert result_dict["message"] == "Test message"
    assert "timestamp" in result_dict 