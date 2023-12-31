"""empty message

Revision ID: f612fecc1649
Revises: 7a61dda1ad8a
Create Date: 2023-07-07 11:16:48.596263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f612fecc1649'
down_revision = '7a61dda1ad8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('id_')

    # ### end Alembic commands ###
