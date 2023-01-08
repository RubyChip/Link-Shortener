"""create url table

Revision ID: 23dfdacd7d78
Revises: 
Create Date: 2023-01-06 19:55:53.498480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23dfdacd7d78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'url',
        sa.Column('unique_code', sa.String, primary_key=True),
        sa.Column('origin_url', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('url')
