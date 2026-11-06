"""
Pydantic models for Dashboard API (MS-3)
Based on actual Flask endpoint schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List


class SliceStateResponse(BaseModel):
    """Response model for slice state"""
    id: int
    slice_id: str
    pipeline: str  # "6G" or "5G"
    qos_score: Optional[float]
    congestion_level: Optional[str]  # "Normal", "Light", "Critical"
    is_anomaly: Optional[bool]
    anomaly_score: Optional[float]
    status: str  # "active", "inactive"
    last_updated: str
    latency_budget: Optional[float]
    slice_latency: Optional[float]
    packet_loss_budget: Optional[float]
    slice_packet_loss: Optional[float]
    jitter_budget: Optional[float]
    slice_jitter: Optional[float]
    data_rate_budget: Optional[float]
    slice_transfer_rate: Optional[float]


class AlertResponse(BaseModel):
    """Response model for alert"""
    id: int
    slice_id: Optional[str]
    level: str  # "WARN" or "CRITICAL"
    message: str
    acknowledged: bool
    created_at: str


class DashboardData(BaseModel):
    """Response model for dashboard data"""
    slices: List[SliceStateResponse]
    alerts: List[AlertResponse]
    timestamp: str
