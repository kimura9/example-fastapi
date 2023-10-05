"""add content column to posts table

Revision ID: 1f8caa01b6d9
Revises: 8b5017996550
Create Date: 2023-10-05 17:17:53.563755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f8caa01b6d9'
down_revision: Union[str, None] = '8b5017996550'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
