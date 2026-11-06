"""
Router for Dashboard endpoints (proxies to MS-3)
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from models import DashboardData
from services import MS3Client

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
ms3_client = MS3Client()


@router.get("/data", response_model=DashboardData)
async def get_dashboard_data() -> DashboardData:
    """
    Get dashboard data (slices and alerts)
    
    Aggregates data from MS-3 endpoints:
    - GET /dashboard/slices
    - GET /dashboard/alerts
    """
    try:
        # Get slices and alerts in parallel
        slices_response = await ms3_client.get_dashboard_slices()
        alerts_response = await ms3_client.get_dashboard_alerts()
        
        return {
            "slices": slices_response["data"],
            "alerts": alerts_response["data"],
            "timestamp": slices_response["timestamp"]
        }
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-3 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/alerts/{alert_id}/acknowledge")
async def acknowledge_alert(alert_id: int):
    """
    Acknowledge an alert
    
    Proxies to MS-3: POST /dashboard/alert/ack
    """
    try:
        result = await ms3_client.acknowledge_alert(alert_id)
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-3 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
