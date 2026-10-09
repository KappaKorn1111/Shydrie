# Shydrie

Shydrie is a distributed, privacy-preserving biometric and environmental data-fusion engine. It compartmentalizes sensitive biometric data, recomputes it alongside NOAA/NASA geospatial data products and RF spectral telemetry, and presents a unified operational picture for analysis while preserving privacy and verifiability.

## Mission

Shydrie separates sensitive personal data from public environmental and sensor streams through strict trust boundaries and policy-driven recomputation. The platform is designed for:

- isolated biometric processing in regulated domains
- public earth-observation and RF ingestion in shared compute planes
- privacy-preserving correlation via de-identification, pseudonymization, and differential privacy
- robust service orchestration for near-real-time fusion
- end-to-end observability and immutable auditability

## Architecture summary

Layer 0 — Application Construction
- shared contracts and schemas
- config management and deployment scaffolding
- containerized services and reproducible builds

Layer 1 — Intelligent Orchestration
- biometric ingest agent
- NOAA/NASA fetcher agent
- RF telemetry agent
- fusion and recomputation agent
- workflow scheduling with Prefect or Ray

Layer 2 — Stability and Control
- zero-trust security and identity enforcement
- isolated biometric execution (TEEs / gVisor / Kata Containers)
- Pydantic + Great Expectations validation
- dead-letter queues and checkpoint-based rollback

Layer 3 — Observability and Management
- OpenTelemetry, Prometheus, Grafana
- immutable audit trail
- lifecycle management and TTL retention
- GitHub Actions and Trivy-based security scanning

## Core technology stack

- Python, NumPy, CuPy, xarray, SciPy, PyTorch
- GNU Radio, SoapySDR
- GDAL, NetCDF4, h5py
- FastAPI, gRPC, Apache Arrow Flight
- TimescaleDB / InfluxDB
- MinIO S3-compatible storage
- Redis Cluster
- React, WebGL, Deck.gl, CesiumJS

## Repository structure

- `apps/api`: FastAPI service layer
- `core`: shared schemas and utility helpers
- `services`: domain service implementations
- `workers`: orchestration and pipeline workers
- `infra/k8s`: deployment manifests
- `docs/architecture`: architecture and governance docs
- `.github/workflows`: CI/CD automation

## Quick start

```bash
docker compose up --build
```

Then open:

- API: `http://localhost:8000/docs`
- MinIO Console: `http://localhost:9001`

## Environment variables

```bash
export POSTGRES_DSN="postgresql://postgres:postgres@localhost:5432/shydrie"
export REDIS_URL="redis://localhost:6379/0"
export MINIO_ENDPOINT="localhost:9000"
export MINIO_ACCESS_KEY="minioadmin"
export MINIO_SECRET_KEY="minioadmin"
export JWT_SECRET="changeme"
```

## Security principles

- raw biometric data remains isolated and encrypted
- identity and authorization are enforced for every service and request
- only de-identified or aggregate data crosses trust boundaries
- all queries and recomputations are logged in an immutable audit trail
- data retention is automated and policy-driven

## License

See `LICENSE` for details.
