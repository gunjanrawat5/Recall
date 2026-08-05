import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    password:str = Field(min_length=8, max_length=128)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: str
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8,max_length=128)
    is_active: bool | None = None

