"""Added followers

Revision ID: b85253d8a492
Revises: 81942401688a
Create Date: 2020-06-18 22:39:27.246565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b85253d8a492'
down_revision = '81942401688a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'followers',
        sa.Column('follower_id', sa.Integer(), nullable=True),
        sa.Column('followed_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
        sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
