# ADR-004: Isolated biometric execution

## Status
Accepted

## Context
Biometric telemetry is high sensitivity and must not be co-located with broad shared compute workloads.

## Decision
Run raw biometric ingestion and recomputation in isolated pods or TEEs, with de-identification and policy enforcement at the boundary.

## Consequences
- improved privacy posture and reduced blast radius
- stronger compliance posture for regulated biometric workloads
- added deployment complexity and operational isolation requirements
