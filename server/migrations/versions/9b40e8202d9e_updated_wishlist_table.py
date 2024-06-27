"""updated Wishlist table

Revision ID: 9b40e8202d9e
Revises: bec7bf7dd9d9
Create Date: 2024-06-27 16:52:17.539931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b40e8202d9e'
down_revision = 'bec7bf7dd9d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_add', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_wishlist_book_id_books'), 'books', ['book_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_wishlist_user_id_users'), 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_wishlist_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_wishlist_book_id_books'), type_='foreignkey')
        batch_op.drop_column('date_add')

    # ### end Alembic commands ###
