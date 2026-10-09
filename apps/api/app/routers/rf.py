from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def rf_status() -> dict:
    return {"status": "RF telemetry service online"}


@router.post("/capture")
def capture_rf(payload: dict):
    return {"status": "accepted", "capture": payload}
