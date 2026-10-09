from datetime import datetime, timedelta
from typing import Any

import jwt
from fastapi import HTTPException, status
from pydantic import BaseModel

from app.config import settings


class TokenPayload(BaseModel):
    sub: str
    exp: datetime
    scope: str


class AuthService:
    def __init__(self, secret: str = settings.jwt_secret):
        self.secret = secret

    def create_token(self, subject: str, scope: str = "read") -> str:
        payload = {
            "sub": subject,
            "scope": scope,
            "exp": datetime.utcnow() + timedelta(hours=1),
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def validate_token(self, token: str) -> TokenPayload:
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return TokenPayload(
                sub=payload["sub"],
                exp=datetime.utcfromtimestamp(payload["exp"]),
                scope=payload.get("scope", "read"),
            )
        except Exception as exc:  # pragma: no cover
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            ) from exc
