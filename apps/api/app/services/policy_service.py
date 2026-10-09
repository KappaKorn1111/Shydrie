from typing import Any

from fastapi import HTTPException, status


class PolicyService:
    def __init__(self) -> None:
        self.allowed_roles = {
            "admin": {"biometric:*", "geospatial:*", "rf:*", "fusion:*", "audit:*"},
            "analyst": {"geospatial:read", "rf:read", "fusion:read", "audit:read"},
            "biometric_only": {"biometric:read", "biometric:write"},
        }

    def authorize(self, subject: str, scope: str, action: str) -> bool:
        role = subject.lower()
        if role not in self.allowed_roles:
            return False

        resource_scope = f"{scope}:{action}"
        if resource_scope in self.allowed_roles[role]:
            return True

        wildcard = f"{scope}:*"
        return wildcard in self.allowed_roles[role]

    def require_access(self, subject: str, scope: str, action: str) -> None:
        if not self.authorize(subject, scope, action):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied for {subject} on {scope}:{action}",
            )
