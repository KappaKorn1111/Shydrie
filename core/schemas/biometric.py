from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class BiometricTelemetry(BaseModel):
    subject_token: str = Field(..., min_length=16)
    timestamp: datetime
    sensor_type: Literal["HR", "GSR", "EEG", "TEMP", "ENV"]
    value: float
    unit: str
    source_device_id: str
    quality_score: float = Field(..., ge=0.0, le=1.0)
    encryption_context: str
    feature_window_id: str


class DeidentifiedBiometricFeature(BaseModel):
    feature_id: str
    subject_token: str
    window_start: datetime
    window_end: datetime
    feature_name: str
    feature_value: float
    feature_type: str
    privacy_level: Literal["pseudonymized", "aggregated", "differentially_private"]
    provenance_id: str
