"""posts table

Revision ID: 0240ec96f499
Revises: db6247c59884
Create Date: 2023-03-13 23:13:05.572953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0240ec96f499'
down_revision = 'db6247c59884'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_posts_timestamp'), ['timestamp'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_username', ['username'], unique=False)
        batch_op.create_index('ix_users_email', ['email'], unique=False)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_posts_timestamp'))

    op.drop_table('posts')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
