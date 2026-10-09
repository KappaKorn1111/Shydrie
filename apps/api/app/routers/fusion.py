from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def fusion_status() -> dict:
    return {"status": "fusion engine online"}


@router.post("/compute")
def compute_fusion(payload: dict):
    return {"status": "accepted", "fusion": payload}
