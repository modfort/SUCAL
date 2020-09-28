"""added courses to user table

Revision ID: 088f8cc1079a
Revises: 4a27612d6ff1
Create Date: 2020-09-27 23:52:46.761546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '088f8cc1079a'
down_revision = '4a27612d6ff1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('courses', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'courses')
    # ### end Alembic commands ###
