from prefect import flow, task


@task
def fetch_satellite_granule():
    return "granule://noaa/test-granule"


@task
def validate_granule(granule):
    return {"status": "valid", "granule": granule}


@task
def generate_raster_tiles(validated):
    return {"status": "tiles_created", "tile_count": 24, "granule": validated["granule"]}


@task
def ingest_biometric_features():
    return {"status": "biometric_features_ready"}


@task
def compute_fusion_context(raster, biometric):
    return {"fusion_context_id": "fusion-001", "score": 0.82}


@flow
def shydrie_pipeline():
    granule = fetch_satellite_granule()
    validated = validate_granule(granule)
    raster = generate_raster_tiles(validated)
    biometric = ingest_biometric_features()
    return compute_fusion_context(raster, biometric)
