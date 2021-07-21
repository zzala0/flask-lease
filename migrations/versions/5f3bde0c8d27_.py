"""empty message

Revision ID: 5f3bde0c8d27
Revises: 
Create Date: 2021-07-21 14:59:49.180230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3bde0c8d27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leasecls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('clsname', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_leasecls')),
    sa.UniqueConstraint('clsname', name=op.f('uq_leasecls_clsname'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('contract',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('startdate', sa.Date(), nullable=False),
    sa.Column('enddate', sa.Date(), nullable=False),
    sa.Column('rate', sa.Numeric(precision=2, scale=10), nullable=False),
    sa.Column('lease_fee', sa.Integer(), nullable=False),
    sa.Column('init_fee', sa.Integer(), nullable=True),
    sa.Column('deposit', sa.Integer(), nullable=True),
    sa.Column('rstr_alwn', sa.Integer(), nullable=True),
    sa.Column('basenode_id', sa.Integer(), nullable=True),
    sa.Column('leasecls_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['leasecls_id'], ['leasecls.id'], name=op.f('fk_contract_leasecls_id_leasecls'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_contract_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_contract'))
    )
    op.create_table('baseline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('startdate', sa.Date(), nullable=False),
    sa.Column('enddate', sa.Date(), nullable=False),
    sa.Column('rate', sa.Numeric(precision=2, scale=10), nullable=False),
    sa.Column('lease_fee', sa.Integer(), nullable=False),
    sa.Column('init_fee', sa.Integer(), nullable=True),
    sa.Column('deposit', sa.Integer(), nullable=True),
    sa.Column('rstr_alwn', sa.Integer(), nullable=True),
    sa.Column('prnt_asset', sa.Integer(), nullable=True),
    sa.Column('prnt_depac', sa.Integer(), nullable=True),
    sa.Column('prnt_lblti', sa.Integer(), nullable=True),
    sa.Column('prnt_dpsit', sa.Integer(), nullable=True),
    sa.Column('prnt_rstra', sa.Integer(), nullable=True),
    sa.Column('basenode_id', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], name=op.f('fk_baseline_contract_id_contract'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_baseline_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_baseline'))
    )
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cycle', sa.Integer(), nullable=True),
    sa.Column('exemonth', sa.Date(), nullable=False),
    sa.Column('lease_fee', sa.Integer(), nullable=True),
    sa.Column('lease_lbt', sa.Integer(), nullable=True),
    sa.Column('lease_exp', sa.Integer(), nullable=True),
    sa.Column('deposit_dscnt', sa.Integer(), nullable=True),
    sa.Column('deposit_intr', sa.Integer(), nullable=True),
    sa.Column('rstr_exp', sa.Integer(), nullable=True),
    sa.Column('rstr_alw', sa.Integer(), nullable=True),
    sa.Column('lease_dep', sa.Integer(), nullable=True),
    sa.Column('dep_accum', sa.Integer(), nullable=True),
    sa.Column('lease_ast', sa.Integer(), nullable=True),
    sa.Column('lease_acq', sa.Integer(), nullable=True),
    sa.Column('inhr', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('baseline_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['baseline_id'], ['baseline.id'], name=op.f('fk_schedule_baseline_id_baseline'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], name=op.f('fk_schedule_contract_id_contract'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_schedule'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    op.drop_table('baseline')
    op.drop_table('contract')
    op.drop_table('user')
    op.drop_table('leasecls')
    # ### end Alembic commands ###
