"""Create tables

Revision ID: daa258197794
Revises: 
Create Date: 2024-02-13 18:06:45.990053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'daa258197794'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('party',
    sa.Column('status_closed', sa.Boolean(), nullable=False),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.Column('task_description', sa.String(), nullable=False),
    sa.Column('line', sa.String(), nullable=False),
    sa.Column('shift', sa.String(), nullable=False),
    sa.Column('brigade', sa.String(), nullable=False),
    sa.Column('party_number', sa.Integer(), nullable=False),
    sa.Column('party_date', sa.Date(), nullable=False),
    sa.Column('nomenclature', sa.String(), nullable=False),
    sa.Column('ecn_code', sa.String(), nullable=False),
    sa.Column('rc_identifier', sa.String(), nullable=False),
    sa.Column('shift_start_datetime', sa.DateTime(), nullable=False),
    sa.Column('shift_end_datetime', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('party_date'),
    sa.UniqueConstraint('party_number')
    )
    op.create_index(op.f('ix_party_id'), 'party', ['id'], unique=False)
    op.create_table('product',
    sa.Column('code_product', sa.String(), nullable=False),
    sa.Column('is_aggregated', sa.Boolean(), nullable=False),
    sa.Column('aggregated_at', sa.DateTime(), nullable=False),
    sa.Column('party_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['party_id'], ['party.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code_product'),
    sa.UniqueConstraint('party_id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_party_id'), table_name='party')
    op.drop_table('party')
    # ### end Alembic commands ###
