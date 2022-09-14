"""empty message

Revision ID: 8bad7045bf7c
Revises: 
Create Date: 2022-09-14 18:14:26.984136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bad7045bf7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('casino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('telefono', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('direccion', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('direccion'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telefono')
    )
    op.create_table('dias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dia', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empresa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('telefono', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('direccion', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('casino_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['casino_id'], ['casino.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('direccion'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('telefono')
    )
    op.create_table('menus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('principal', sa.String(length=180), nullable=False),
    sa.Column('ensalada', sa.String(length=180), nullable=False),
    sa.Column('postre', sa.String(length=180), nullable=False),
    sa.Column('bebida', sa.String(length=180), nullable=False),
    sa.Column('dia_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dia_id'], ['dias.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ensalada'),
    sa.UniqueConstraint('postre'),
    sa.UniqueConstraint('principal')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('apellido', sa.String(length=80), nullable=False),
    sa.Column('telefono', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('direccion', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('empresa_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['empresa_id'], ['empresa.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('direccion'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telefono')
    )
    op.create_table('decision__almuerzo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('decision', sa.String(length=120), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reporte__usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contenido', sa.String(length=120), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reporte__usuario')
    op.drop_table('decision__almuerzo')
    op.drop_table('usuarios')
    op.drop_table('menus')
    op.drop_table('empresa')
    op.drop_table('dias')
    op.drop_table('casino')
    # ### end Alembic commands ###
