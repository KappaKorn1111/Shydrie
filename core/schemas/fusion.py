from datetime import datetime

from pydantic import BaseModel, Field


class FusionEvent(BaseModel):
    fusion_event_id: str
    subject_token: str
    environmental_context_id: str
    rf_context_id: str
    time_window: str
    biometric_feature_vector: dict
    environmental_feature_vector: dict
    fusion_score: float = Field(..., ge=0.0, le=1.0)
    confidence: float = Field(..., ge=0.0, le=1.0)
    recomputation_version: str
    policy_decision: str
    audit_log_ref: str
