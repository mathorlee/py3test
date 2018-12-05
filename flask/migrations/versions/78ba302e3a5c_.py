"""empty message

Revision ID: 78ba302e3a5c
Revises: ea70c2ce6a17
Create Date: 2018-12-02 22:19:32.563113

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '78ba302e3a5c'
down_revision = 'ea70c2ce6a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('student_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'score', ['student_id', 'cource_id'])
    op.drop_constraint('score_ibfk_2', 'score', type_='foreignkey')
    op.create_foreign_key(None, 'score', 'student', ['student_id'], ['id'])
    op.drop_column('score', 'table_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('table_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'score', type_='foreignkey')
    op.create_foreign_key('score_ibfk_2', 'score', 'student', ['table_id'], ['id'])
    op.drop_constraint(None, 'score', type_='unique')
    op.drop_column('score', 'student_id')
    # ### end Alembic commands ###