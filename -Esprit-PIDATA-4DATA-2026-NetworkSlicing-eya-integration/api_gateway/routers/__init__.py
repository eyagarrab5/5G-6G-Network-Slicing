"""Routers package"""
from .predictions import router as predictions_router
from .anomalies import router as anomalies_router
from .dashboard import router as dashboard_router

__all__ = ["predictions_router", "anomalies_router", "dashboard_router"]
