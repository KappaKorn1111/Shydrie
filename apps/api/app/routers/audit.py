from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def audit_status() -> dict:
    return {"status": "audit service online"}


@router.get("/events")
def list_events() -> dict:
    return {"events": []}
