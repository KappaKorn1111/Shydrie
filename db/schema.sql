CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS biometric_telemetry (
    id BIGSERIAL PRIMARY KEY,
    subject_token TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    sensor_type TEXT NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    unit TEXT NOT NULL,
    source_device_id TEXT NOT NULL,
    quality_score DOUBLE PRECISION NOT NULL,
    encryption_context TEXT NOT NULL,
    feature_window_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS biometric_features (
    id BIGSERIAL PRIMARY KEY,
    subject_token TEXT NOT NULL,
    window_start TIMESTAMPTZ NOT NULL,
    window_end TIMESTAMPTZ NOT NULL,
    feature_name TEXT NOT NULL,
    feature_value DOUBLE PRECISION NOT NULL,
    feature_type TEXT NOT NULL,
    privacy_level TEXT NOT NULL,
    provenance_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS geospatial_granules (
    id BIGSERIAL PRIMARY KEY,
    granule_id TEXT UNIQUE NOT NULL,
    provider TEXT NOT NULL,
    platform TEXT NOT NULL,
    acquisition_time TIMESTAMPTZ NOT NULL,
    spatial_bounds TEXT NOT NULL,
    resolution DOUBLE PRECISION NOT NULL,
    file_uri TEXT NOT NULL,
    checksum TEXT NOT NULL,
    metadata_hash TEXT NOT NULL,
    processing_level TEXT NOT NULL,
    data_quality_score DOUBLE PRECISION NOT NULL
);

CREATE TABLE IF NOT EXISTS rf_captures (
    id BIGSERIAL PRIMARY KEY,
    capture_id TEXT UNIQUE NOT NULL,
    device_id TEXT NOT NULL,
    center_frequency DOUBLE PRECISION NOT NULL,
    gain DOUBLE PRECISION NOT NULL,
    sampling_rate DOUBLE PRECISION NOT NULL,
    iq_sample_count INTEGER NOT NULL,
    timestamp_start TIMESTAMPTZ NOT NULL,
    timestamp_end TIMESTAMPTZ NOT NULL,
    file_uri TEXT NOT NULL,
    checksum TEXT NOT NULL,
    fft_resolution INTEGER NOT NULL,
    spectral_window TEXT NOT NULL,
    quality_score DOUBLE PRECISION NOT NULL
);

CREATE TABLE IF NOT EXISTS fusion_events (
    id BIGSERIAL PRIMARY KEY,
    fusion_event_id TEXT UNIQUE NOT NULL,
    subject_token TEXT NOT NULL,
    environmental_context_id TEXT NOT NULL,
    rf_context_id TEXT NOT NULL,
    time_window TEXT NOT NULL,
    biometrics_json JSONB NOT NULL,
    environment_json JSONB NOT NULL,
    fusion_score DOUBLE PRECISION NOT NULL,
    confidence DOUBLE PRECISION NOT NULL,
    recomputation_version TEXT NOT NULL,
    policy_decision TEXT NOT NULL,
    audit_log_ref TEXT NOT NULL
);

SELECT create_hypertable('biometric_telemetry', 'timestamp');
SELECT create_hypertable('biometric_features', 'window_start');
SELECT create_hypertable('rf_captures', 'timestamp_start');
