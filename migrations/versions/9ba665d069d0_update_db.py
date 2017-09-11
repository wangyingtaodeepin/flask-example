"""update db

Revision ID: 9ba665d069d0
Revises: 3f2bc19c03b5
Create Date: 2017-09-11 14:12:47.864474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba665d069d0'
down_revision = '3f2bc19c03b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
