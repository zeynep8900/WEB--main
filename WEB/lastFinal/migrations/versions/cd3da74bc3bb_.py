"""empty message

Revision ID: cd3da74bc3bb
Revises: 0301c959073c
Create Date: 2024-05-26 00:38:56.538722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd3da74bc3bb'
down_revision = '0301c959073c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_info',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('address', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###