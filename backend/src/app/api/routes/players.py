from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.service.player_service import(create_player, get_by_squad_number)
from app.db.session import get_async_session
from app.schemas.player import PlayerCreate, PlayerResponse
from app.models.player import Player


router = APIRouter(
    prefix="/players",
    tags=["Players"],
)


@router.post(
    "/",
    response_model=PlayerResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_player_endpoint(
    player_data: PlayerCreate,
    response: Response,
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> Player:
    existing = await get_by_squad_number(
        session,
        player_data.team_number,
    )

    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A player with this squad number already exists.",
        )

    player = await create_player(session, player_data)

    response.headers["Location"] = f"/players/{player.id}"
    return player