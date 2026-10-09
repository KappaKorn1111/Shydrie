# ADR-001: Platform and language selection

## Status
Accepted

## Context
Shydrie requires a mix of high-throughput streaming, geospatial analysis, GPU-capable DSP, and strongly typed schema validation.

## Decision
We use Python as the primary compute language with NumPy, CuPy, SciPy, xarray, PyTorch, FastAPI, and gRPC. We also use React for the dashboard and Redis/MinIO/TimescaleDB for storage and messaging.

## Consequences
- strong scientific and data-engineering ecosystem
- good fit for DSP, geospatial parsing, and ML pipelines
- requires disciplined dependency and version management
- must enforce strong schema validation and secure runtime controls
