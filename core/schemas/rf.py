from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class RFCapture(BaseModel):
    capture_id: str
    device_id: str
    center_frequency: float
    gain: float
    sampling_rate: float
    iq_sample_count: int
    timestamp_start: datetime
    timestamp_end: datetime
    file_uri: str
    checksum: str
    fft_resolution: int
    spectral_window: str
    quality_score: float = Field(..., ge=0.0, le=1.0)


class SpectrogramFrame(BaseModel):
    frame_id: str
    capture_id: str
    window_start: datetime
    window_end: datetime
    image_uri: str
    fft_size: int
    sample_rate: int
    band_type: Literal["waterfall", "spectrogram"]
