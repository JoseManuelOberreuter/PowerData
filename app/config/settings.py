# Configuration settings for the health check service 

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Application info
    app_name: str = "Health Check Service"
    app_version: str = "1.0.0"
    
    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    # Health check message
    health_message: str = "Service is running normally"
    
    class Config:
        env_file = ".env"


# Global settings instance
settings = Settings() 