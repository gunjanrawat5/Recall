from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session
from app.core.security.jwt import create_access_token
from app.core.security.password import verify_password
from app.schemas.auth import LoginRequest, TokenResponse
from app.service.user_service import UserService


class AuthService:
    def __init__(
        self,
        db: AsyncSession,
    ) -> None:
        self.db = db
        self.user_service = UserService(db)

    async def login(
        self,
        login_data: LoginRequest,
    ) -> TokenResponse:

        user = await self.user_service.get_user_by_email(
            login_data.email
        )

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            login_data.password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is inactive")

        access_token = create_access_token(
            str(user.id)
        )

        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
        )

def get_auth_service(
    db: AsyncSession = Depends(get_async_session),
) -> AuthService:
    return AuthService(db)