from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.auth import LoginRequest, TokenResponse
from app.service.auth_service import AuthService, get_auth_service
from app.core.security.current_user import get_current_user
from app.models import User
from app.schemas import UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenResponse:

    try:
        return await auth_service.login(login_data)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc

@router.get(
    "/me",
    response_model=UserResponse,
)
async def get_me(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user