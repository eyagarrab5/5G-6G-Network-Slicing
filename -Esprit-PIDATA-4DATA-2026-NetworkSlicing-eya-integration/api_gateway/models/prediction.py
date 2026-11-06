"""
Pydantic models for Prediction API (MS-1)
Based on actual Flask endpoint schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List


class PredictionRequest6G(BaseModel):
    """Request model for 6G QoS prediction"""
    slice_id: Optional[str] = Field(None, description="Slice identifier")
    latency_budget: float = Field(..., ge=0, description="Latency budget in microseconds")
    slice_latency: float = Field(..., ge=0, description="Actual slice latency in microseconds")
    packet_loss_budget: float = Field(..., ge=0, le=1, description="Packet loss budget")
    slice_packet_loss: float = Field(..., ge=0, le=1, description="Actual slice packet loss")
    jitter_budget: float = Field(..., ge=0, description="Jitter budget in microseconds")
    slice_jitter: float = Field(..., ge=0, description="Actual slice jitter in microseconds")
    data_rate_budget: float = Field(..., ge=0, description="Data rate budget in Gbps")
    slice_transfer_rate: float = Field(..., ge=0, description="Actual slice transfer rate in Gbps")


class PredictionRequest5G(BaseModel):
    """Request model for 5G QoS prediction"""
    slice_id: Optional[str] = Field(None, description="Slice identifier")
    plr: float = Field(..., ge=0, le=1, description="Packet loss rate")
    delay: float = Field(..., ge=0, description="Packet delay in ms")
    time: int = Field(..., ge=0, le=23, description="Hour of day (0-23)")
    lte5g_cat: int = Field(..., ge=0, description="LTE/5G category")


class CongestionRequest(BaseModel):
    """Request model for congestion prediction"""
    slice_id: Optional[str] = Field(None, description="Slice identifier")
    latency_budget: float = Field(..., ge=0)
    slice_latency: float = Field(..., ge=0)
    packet_loss_budget: float = Field(..., ge=0, le=1)
    slice_packet_loss: float = Field(..., ge=0, le=1)
    jitter_budget: float = Field(..., ge=0)
    slice_jitter: float = Field(..., ge=0)
    data_rate_budget: float = Field(..., ge=0)
    slice_transfer_rate: float = Field(..., ge=0)
    required_mobility: Optional[float] = Field(0, ge=0)
    required_connectivity: Optional[float] = Field(1, ge=0)
    slice_type: Optional[int] = Field(0)
    slice_handover: Optional[int] = Field(0)


class PredictionResponse(BaseModel):
    """Response model for QoS prediction"""
    slice_id: str
    qos_score: float
    congestion_level: str  # "Normal", "Light", "Critical"
    sla_respected: Optional[bool] = None
    risk_level: Optional[str] = None
    p_sla_met: Optional[float] = None
    qos_risk_score: Optional[float] = None
    risk_tier: Optional[str] = None
    pipeline: Optional[str] = None  # "5G" or "6G"


class PredictionStats(BaseModel):
    """Response model for prediction statistics"""
    total_predictions: int
    by_congestion_level: dict
    qos_stats: dict
    sla_compliance_rate: float


class CongestionResponse(BaseModel):
    """Response model for congestion prediction"""
    slice_id: str
    congestion_level: str  # "Normal", "Light", "Critical"
    confidence: float
    raw_class: str
