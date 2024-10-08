"""make email not unique

Revision ID: 12f1aeea7371
Revises: 7388eba5e696
Create Date: 2024-09-08 14:45:44.921637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12f1aeea7371'
down_revision = '7388eba5e696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.create_index('ix_users_email', ['email'], unique=1)

    # ### end Alembic commands ###
