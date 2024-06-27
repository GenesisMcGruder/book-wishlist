"""updated Wishlist table#2

Revision ID: 992204f94e9f
Revises: 9b40e8202d9e
Create Date: 2024-06-27 17:39:33.032988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '992204f94e9f'
down_revision = '9b40e8202d9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_wishlists_book_id_books')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_wishlists_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('wishlist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishlist',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('book_id', sa.INTEGER(), nullable=True),
    sa.Column('date_add', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='fk_wishlist_book_id_books'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_wishlist_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('wishlists')
    # ### end Alembic commands ###
