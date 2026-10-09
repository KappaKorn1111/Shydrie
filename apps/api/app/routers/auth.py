from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from app.config import settings
from app.deps import get_current_token
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

auth_service = AuthService(settings.jwt_secret)


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/token")
def login(payload: LoginRequest):
    if payload.username == "admin" and payload.password == "admin":
        token = auth_service.create_token(payload.username, scope="admin")
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.get("/whoami")
def who_am_i(subject: str = Depends(get_current_token)):
    return {"subject": subject}
