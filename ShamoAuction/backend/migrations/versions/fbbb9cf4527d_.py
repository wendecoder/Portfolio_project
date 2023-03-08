"""empty message

Revision ID: fbbb9cf4527d
Revises: 
Create Date: 2023-02-19 02:13:02.294082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbbb9cf4527d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('Category', sa.String(), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('ImageLink', sa.String(), nullable=True),
    sa.Column('StartingBid', sa.Integer(), nullable=True),
    sa.Column('AuctionBeginingDate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('AuctionEndingDate', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('UserName', sa.String(), nullable=True),
    sa.Column('Password', sa.String(), nullable=True),
    sa.Column('Address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('items')
    # ### end Alembic commands ###