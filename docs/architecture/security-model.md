# Security model

## Zero-trust principles

- every service authenticates
- every request is authorized at the policy layer
- no raw biometric access without explicit policy approval
- direct identifiers are removed before cross-domain transfer
- all access decisions are logged and auditable

## Data classification

1. Tier 0 — raw biometric telemetry
2. Tier 1 — pseudonymized biometric features
3. Tier 2 — geospatial products
4. Tier 3 — RF capture files
5. Tier 4 — aggregate fused outputs

## Enforcement

- OAuth2/JWT for user access
- mTLS or strong service identity for internal calls
- RBAC with least privilege
- TEE or isolated container execution for Tier 0 workloads
- policy denial by default
