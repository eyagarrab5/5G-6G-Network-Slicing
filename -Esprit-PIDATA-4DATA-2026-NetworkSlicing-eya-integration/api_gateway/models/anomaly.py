"""
Pydantic models for Anomaly Detection API (MS-2)
Based on actual Flask endpoint schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


class AnomalyDetectRequest(BaseModel):
    """Request model for anomaly detection"""
    slice_id: Optional[str] = Field(None, description="Slice identifier")
    features: Dict[str, float] = Field(..., description="Network features")


class AnomalyMethodResult(BaseModel):
    """Result from a single anomaly detection method"""
    is_anomaly: bool
    score: float


class AnomalyDetectResponse(BaseModel):
    """Response model for anomaly detection"""
    is_anomaly: bool
    score: float
    confidence: float
    method: str
    anomaly_id: Optional[int] = None
    methods: Dict[str, AnomalyMethodResult]


class AnomalyHistoryRequest(BaseModel):
    """Request model for anomaly history query"""
    slice_id: Optional[str] = None
    is_anomaly: Optional[bool] = None
    method: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    limit: int = Field(100, ge=1, le=500)
    offset: int = Field(0, ge=0)


class AnomalyRecord(BaseModel):
    """Single anomaly record"""
    id: int
    slice_id: str
    score: float
    is_anomaly: bool
    method: str
    isolation_forest_score: float
    autoencoder_score: float
    features_json: str
    created_at: str


class AnomalyHistoryResponse(BaseModel):
    """Response model for anomaly history"""
    total: int
    count: int
    anomalies: List[AnomalyRecord]


class AnomalyStatsResponse(BaseModel):
    """Response model for anomaly statistics"""
    total_detections: int
    total_anomalies: int
    anomaly_rate: float
    by_slice: Dict[str, Dict[str, Any]]
    by_method: Dict[str, int]
    by_period: List[Dict[str, Any]]
    period: str
    days: int
