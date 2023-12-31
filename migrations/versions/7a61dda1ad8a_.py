"""empty message

Revision ID: 7a61dda1ad8a
Revises: f7ea8548b6e9
Create Date: 2023-07-07 11:07:46.916252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a61dda1ad8a'
down_revision = 'f7ea8548b6e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    with op.batch_alter_table('like', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('like', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('article_tag', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###
