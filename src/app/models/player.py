import uuid 

from sqlalchemy import Integer,String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Player(Base):
    __tablename__ = "players"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    team_number: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=False
    )
