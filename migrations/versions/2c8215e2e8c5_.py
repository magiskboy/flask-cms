"""empty message

Revision ID: 2c8215e2e8c5
Revises: f612fecc1649
Create Date: 2023-07-07 11:17:50.398048

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2c8215e2e8c5'
down_revision = 'f612fecc1649'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.drop_column('id_')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###
