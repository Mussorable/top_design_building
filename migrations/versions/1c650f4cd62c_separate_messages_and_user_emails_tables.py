"""separate messages and user emails tables

Revision ID: 1c650f4cd62c
Revises: 5d8f3b095695
Create Date: 2024-09-12 21:54:38.369412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c650f4cd62c'
down_revision = '5d8f3b095695'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text_message', sa.String(length=450), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('contact_email_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact_email_id'], ['contact_emails.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('text_message')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text_message', sa.VARCHAR(length=450), nullable=True))

    op.drop_table('messages')
    # ### end Alembic commands ###
