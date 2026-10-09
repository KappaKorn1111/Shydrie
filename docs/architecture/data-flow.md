# Data flow

1. Sensors emit biometric telemetry
2. Ingestion validates and encrypts raw data
3. Privacy filters remove direct identifiers
4. Derived features are emitted for downstream use
5. NOAA/NASA fetcher stages geospatial granules
6. RF service captures I/Q and computes FFT output
7. Fusion engine correlates time-aligned features
8. Results are persisted with provenance information
9. Observability stack records all execution and access events
10. Lifecycle policies enforce retention and purge rules
