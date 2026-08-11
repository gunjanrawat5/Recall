from fastapi import Depends
from app.db.session import get_async_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from app.schemas import UserCreate
from app.schemas import UserUpdate
from app.models import User
from app.core.security.hash_password import hash_password


class UserService:
    def __init__(self, db:AsyncSession) -> None:
        self.db = db

    async def get_user_by_id(self, id: uuid.UUID) -> User | None:
        user = await self.db.get(User,id)
        return user

    async def get_user_by_email(self, email:str) -> User| None:
        statement = select(User).where(User.email == email)
        result = await self.db.execute(statement)
        return result.scalar_one_or_none()

    async def delete_user(self, id: uuid.UUID) -> None:
        user = await self.get_user_by_id(id)

        await self.db.delete(user)
        await self.db.commit()

    async def create_user(self, user_data: UserCreate) -> User:
        exisiting_user = await self.get_user_by_email(user_data.email)
        if exisiting_user is not None:
            raise ValueError("User already exists")

        user = User(
            email = user_data.email,
            password_hash = hash_password(user_data.password),
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_user(
        self,
        user_id: uuid.UUID,
        user_data: UserUpdate,
        ) -> User:
        user = await self.get_user_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        update_data = user_data.model_dump(exclude_unset=True)

        if "email" in update_data:
            existing_user = await self.get_user_by_email(
                update_data["email"]
            )

            if existing_user is not None and existing_user.id != user.id:
                raise ValueError("A user with this email already exists")

            user.email = update_data["email"]

        if "password" in update_data:
            user.password_hash = hash_password(
                update_data["password"]
            )

        if "is_active" in update_data:
            user.is_active = update_data["is_active"]

        await self.db.commit()
        await self.db.refresh(user)

        return user

def get_user_service(
            db: AsyncSession = Depends(get_async_session)
    ) -> UserService:
        return UserService(db)
    
    