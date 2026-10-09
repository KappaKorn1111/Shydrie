from fastapi import FastAPI
from app.routers import biometric, geospatial, rf, fusion, audit

app = FastAPI(
    title="Shydrie API",
    version="0.1.0",
    description="Privacy-preserving biometric and environmental data-fusion platform",
)

app.include_router(biometric.router, prefix="/biometric", tags=["biometric"])
app.include_router(geospatial.router, prefix="/geospatial", tags=["geospatial"])
app.include_router(rf.router, prefix="/rf", tags=["rf"])
app.include_router(fusion.router, prefix="/fusion", tags=["fusion"])
app.include_router(audit.router, prefix="/audit", tags=["audit"])


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
