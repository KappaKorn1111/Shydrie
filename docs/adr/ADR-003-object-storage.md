# ADR-003: Object storage for Earth observation data

## Status
Accepted

## Context
NOAA/NASA granules and RF captures are large binary products that benefit from object storage and immutable versioning.

## Decision
Use MinIO as the S3-compatible storage backend for raw and processed product artifacts.

## Consequences
- simple durability and lifecycle policies
- compatibility with S3 tooling and object APIs
- natural fit for tiled raster outputs and spectrogram artifacts
