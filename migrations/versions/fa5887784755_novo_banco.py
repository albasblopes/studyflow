"""Novo banco

Revision ID: fa5887784755
Revises: 8d264b08f6f5
Create Date: 2023-05-31 16:52:36.524274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa5887784755'
down_revision = '8d264b08f6f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cicloassunto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_ciclo', sa.Integer(), nullable=True),
    sa.Column('id_assunto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_assunto'], ['assunto.id'], ),
    sa.ForeignKeyConstraint(['id_ciclo'], ['cicloestudo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ciclo_assunto')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ciclo_assunto',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('id_ciclo', sa.INTEGER(), nullable=True),
    sa.Column('id_assunto', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['id_assunto'], ['assunto.id'], ),
    sa.ForeignKeyConstraint(['id_ciclo'], ['cicloestudo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cicloassunto')
    # ### end Alembic commands ###
