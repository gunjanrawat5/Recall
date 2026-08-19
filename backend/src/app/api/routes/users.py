from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_session
from app.schemas import UserUpdate, UserCreate, UserResponse
from app.models import User
from app.service.user_service import UserService, get_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model= UserResponse,
    status_code= status.HTTP_201_CREATED,
)
async def create_user(
    user_data: UserCreate,
    user_service : UserService = Depends(get_user_service)
) -> User:
    return await user_service.create_user(user_data)

@router.get(
    "/id/{user_id}",
    response_model=UserResponse,
)
async def get_user_by_id(
    user_id: uuid.UUID,
    user_service : UserService = Depends(get_user_service)
) -> User:
    user = await user_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.get(
    "/email/{email}",
    response_model=UserResponse,
)
async def get_user_by_email(
    email : str,
    user_service: UserService = Depends(get_user_service)
) -> User:
    user = await user_service.get_user_by_email(email)
    if user is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
        )
    return user

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user(
    user_id: uuid.UUID,
    user_data: UserUpdate,
    user_service : UserService = Depends(get_user_service)
) -> User:
    return await user_service.update_user(user_id = user_id, user_data=user_data)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    user_id : uuid.UUID,
    user_service: UserService = Depends(get_user_service)
) -> Response:
    await user_service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
