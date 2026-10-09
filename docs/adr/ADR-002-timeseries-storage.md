# ADR-002: Time-series storage

## Status
Accepted

## Context
The platform ingests high-volume physiological and environmental telemetry with time alignment needs and storage query requirements.

## Decision
Use TimescaleDB as the canonical time-series store for sensor and derived data. InfluxDB may optionally be used for operational metric ingestion.

## Consequences
- natural time-series query performance
- strong support for aggregations over windows and intervals
- easier policy enforcement and retention management for time-bounded sensor data
