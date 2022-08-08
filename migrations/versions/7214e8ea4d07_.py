"""empty message

Revision ID: 7214e8ea4d07
Revises: 7227779daac2
Create Date: 2022-08-04 20:30:11.361090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7214e8ea4d07'
down_revision = '7227779daac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    # ### end Alembic commands ###
