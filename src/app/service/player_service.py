from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.player import Player
from app.schemas.player import PlayerCreate


async def get_by_squad_number(
    session: AsyncSession,
    team_number: int,
) -> Player | None:
    statement = select(Player).where(
        Player.team_number == team_number
    )

    result = await session.execute(statement)
    return result.scalar_one_or_none()


async def create_player(
    session: AsyncSession,
    player_data: PlayerCreate,
) -> Player:
    player = Player(
        name=player_data.name,
        team_number=player_data.team_number,
    )

    session.add(player)
    await session.commit()
    await session.refresh(player)

    return player