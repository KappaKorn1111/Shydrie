from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def geospatial_status() -> dict:
    return {"status": "geospatial service online"}


@router.post("/fetch")
def fetch_granule(payload: dict):
    return {"status": "accepted", "granule": payload}
