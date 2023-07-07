"""empty message

Revision ID: 2b374a5d65f2
Revises: 2c8215e2e8c5
Create Date: 2023-07-07 11:24:10.427281

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2b374a5d65f2'
down_revision = '2c8215e2e8c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('like')
    op.drop_table('article_tag')
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_constraint('article_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('article_ibfk_1', type_='foreignkey')
        batch_op.drop_column('author_id')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('article_ibfk_1', 'user', ['author_id'], ['id'])
        batch_op.create_foreign_key('article_ibfk_2', 'category', ['category_id'], ['id'])

    op.create_table('article_tag',
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='article_tag_ibfk_1'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='article_tag_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('like',
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='like_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='like_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('comment',
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='comment_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='comment_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###