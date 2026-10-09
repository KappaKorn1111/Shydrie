from datetime import datetime

from pydantic import BaseModel, Field


class GeospatialGranule(BaseModel):
    granule_id: str
    product_name: str
    provider: str
    platform: str
    acquisition_time: datetime
    spatial_bounds: str
    resolution: float
    file_uri: str
    checksum: str
    metadata_hash: str
    processing_level: str
    data_quality_score: float = Field(..., ge=0.0, le=1.0)


class GeospatialTile(BaseModel):
    tile_id: str
    granule_id: str
    tile_index: str
    output_path: str
    created_at: datetime
