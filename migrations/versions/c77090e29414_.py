"""empty message

Revision ID: c77090e29414
Revises: 
Create Date: 2018-03-21 16:56:53.288521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c77090e29414'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.Column('created_on', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###