"""
FastAPI Gateway for Network Slicing Platform
Acts as API Gateway / Backend-for-Frontend
Proxies requests to existing Flask microservices
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import predictions_router, anomalies_router, dashboard_router

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API Gateway for 5G/6G Network Slicing Platform. Proxies to existing Flask microservices.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(predictions_router, prefix=settings.API_PREFIX)
app.include_router(anomalies_router, prefix=settings.API_PREFIX)
app.include_router(dashboard_router, prefix=settings.API_PREFIX)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "services": {
            "ms1_predictions": f"{settings.MS1_URL}",
            "ms2_anomalies": f"{settings.MS2_URL}",
            "ms3_dashboard": f"{settings.MS3_URL}",
            "ms5_models": f"{settings.MS5_URL}"
        },
        "docs": "/docs",
        "api_prefix": settings.API_PREFIX
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "ms1": settings.MS1_URL,
            "ms2": settings.MS2_URL,
            "ms3": settings.MS3_URL,
            "ms5": settings.MS5_URL
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
