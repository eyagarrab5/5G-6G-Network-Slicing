"""
Router for Anomaly Detection endpoints (proxies to MS-2)
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, Optional
from models import (
    AnomalyDetectRequest,
    AnomalyDetectResponse,
    AnomalyHistoryResponse,
    AnomalyStatsResponse
)
from services import MS2Client

router = APIRouter(prefix="/anomalies", tags=["anomalies"])
ms2_client = MS2Client()


@router.post("/detect", response_model=AnomalyDetectResponse)
async def detect_anomaly(request: AnomalyDetectRequest):
    """
    Detect anomaly in network metrics
    
    Proxies to MS-2: POST /api/anomaly/detect
    """
    try:
        data = request.model_dump()
        result = await ms2_client.detect_anomaly(data)
        return result["data"]
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-2 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history", response_model=AnomalyHistoryResponse)
async def get_anomaly_history(
    slice_id: Optional[str] = Query(None),
    is_anomaly: Optional[bool] = Query(None),
    method: Optional[str] = Query(None),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0)
) -> AnomalyHistoryResponse:
    """
    Get anomaly detection history
    
    Proxies to MS-2: GET /api/anomaly/history
    """
    try:
        result = await ms2_client.get_anomaly_history(
            slice_id=slice_id,
            is_anomaly=is_anomaly,
            method=method,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            offset=offset
        )
        return result["data"]
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-2 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats", response_model=AnomalyStatsResponse)
async def get_anomaly_stats(
    slice_id: Optional[str] = Query(None),
    period: str = Query("jour"),
    days: int = Query(7, ge=1, le=30)
) -> AnomalyStatsResponse:
    """
    Get anomaly statistics
    
    Proxies to MS-2: GET /api/anomaly/stats
    """
    try:
        result = await ms2_client.get_anomaly_stats(
            slice_id=slice_id,
            period=period,
            days=days
        )
        return result["data"]
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-2 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
