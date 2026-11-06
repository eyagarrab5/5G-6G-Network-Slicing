"""
Router for Prediction endpoints (proxies to MS-1)
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any
from models import (
    PredictionRequest6G,
    PredictionRequest5G,
    PredictionResponse,
    PredictionStats,
    CongestionRequest,
    CongestionResponse
)
from services import MS1Client

router = APIRouter(prefix="/predictions", tags=["predictions"])
ms1_client = MS1Client()


@router.post("/qos/6g", response_model=PredictionResponse)
async def predict_qos_6g(request: PredictionRequest6G):
    """
    Predict QoS for 6G network slice
    
    Proxies to MS-1: POST /predict/qos
    """
    try:
        data = request.model_dump()
        result = await ms1_client.predict_qos_6g(data)
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-1 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/qos/5g", response_model=PredictionResponse)
async def predict_qos_5g(request: PredictionRequest5G):
    """
    Predict QoS for 5G network slice
    
    Proxies to MS-1: POST /predict/qos/5g
    """
    try:
        data = request.model_dump()
        result = await ms1_client.predict_qos_5g(data)
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-1 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/congestion", response_model=CongestionResponse)
async def predict_congestion(request: CongestionRequest):
    """
    Predict congestion level for network slice
    
    Proxies to MS-1: POST /predict/congestion
    """
    try:
        data = request.model_dump()
        result = await ms1_client.predict_congestion(data)
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-1 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
async def get_prediction_history(
    limit: int = Query(50, ge=1, le=100)
) -> Dict[str, Any]:
    """
    Get prediction history
    
    Proxies to MS-1: GET /predict/history
    """
    try:
        result = await ms1_client.get_prediction_history(limit)
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-1 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats", response_model=PredictionStats)
async def get_prediction_stats():
    """
    Get prediction statistics
    
    Proxies to MS-1: GET /predict/stats
    """
    try:
        result = await ms1_client.get_prediction_stats()
        return result
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(status_code=503, detail=f"MS-1 service unavailable: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
