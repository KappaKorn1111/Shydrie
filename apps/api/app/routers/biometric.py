from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def biometric_status() -> dict:
    return {"status": "biometric service online"}


@router.post("/ingest")
def ingest_biometric(payload: dict, token: str = None):
    return {
        "status": "accepted",
        "payload": payload,
        "token_subject": token,
    }
