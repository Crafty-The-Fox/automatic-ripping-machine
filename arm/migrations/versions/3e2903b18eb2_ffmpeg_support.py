"""ffmpeg support

Revision ID: 3e2903b18eb2
Revises: b326a3663939
Create Date: 2024-05-25 21:11:10.985204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e2903b18eb2'
down_revision = 'b326a3663939'
branch_labels = None
depends_on = None


def upgrade():
    sa.Column('FFMPEG_CLI', sa.String(length=256), nullable=True),
    sa.Column('FFMPEG_LOCAL', sa.String(length=256), nullable=True),
    sa.Column('USE_FFMPEG', sa.Boolean(), nullable=True),
    sa.Column('FFMPEG_ARGS', sa.String(length=512), nullable=True),
    pass


def downgrade():
    pass
