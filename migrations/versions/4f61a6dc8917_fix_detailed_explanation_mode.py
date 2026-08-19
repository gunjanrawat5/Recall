"""fix detailed explanation mode

Revision ID: 4f61a6dc8917
Revises: 4bae1798dd78
Create Date: 2026-08-16 18:57:19.126627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f61a6dc8917'
down_revision: Union[str, Sequence[str], None] = '4bae1798dd78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "ALTER TYPE explanation_mode "
        "RENAME VALUE 'deatiled' TO 'detailed'"
    )

def downgrade() -> None:
    """Downgrade schema."""
    pass
