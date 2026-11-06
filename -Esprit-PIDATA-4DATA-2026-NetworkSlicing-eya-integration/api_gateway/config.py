"""
Configuration for FastAPI Gateway
Environment variables and service URLs
"""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # FastAPI Gateway
    APP_NAME: str = "Network Slicing API Gateway"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Service URLs (existing Flask microservices)
    MS1_URL: str = os.environ.get("MS1_URL", "http://localhost:5001")
    MS2_URL: str = os.environ.get("MS2_URL", "http://localhost:5000")
    MS3_URL: str = os.environ.get("MS3_URL", "http://localhost:5003")
    MS5_URL: str = os.environ.get("MS5_URL", "http://localhost:5005")
    
    # Database (shared with Flask services - for reference only)
    # FastAPI will NOT connect directly to DB, only via Flask services
    DB_NAME: str = os.environ.get("DB_NAME", "network_slicing_")
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost", "http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000", "http://127.0.0.1"]
    
    # Timeouts
    REQUEST_TIMEOUT: float = 30.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
