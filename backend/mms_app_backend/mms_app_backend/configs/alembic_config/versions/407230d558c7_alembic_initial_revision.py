"""Alembic initial revision

Revision ID: 407230d558c7
Revises: 
Create Date: 2023-04-20 05:22:24.271238

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '407230d558c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_index('ix_criteria_id', table_name='criteria')
    op.drop_table('criteria')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_locations_id', table_name='locations')
    op.drop_table('locations')
    op.drop_index('ix_mentor_managers_id', table_name='mentor_managers')
    op.drop_table('mentor_managers')
    op.drop_index('ix_roles_id', table_name='roles')
    op.drop_table('roles')
    op.drop_table('social_links')
    op.drop_index('ix_mentors_id', table_name='mentors')
    op.drop_table('mentors')
    op.drop_index('ix_programs_id', table_name='programs')
    op.drop_table('programs')
    op.drop_index('ix_program_mentor_association_id', table_name='program_mentor_association')
    op.drop_table('program_mentor_association')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('program_mentor_association',
    sa.Column('program_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mentor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['mentor_id'], ['mentors.id'], name='program_mentor_association_mentor_id_fkey'),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], name='program_mentor_association_program_id_fkey'),
    sa.PrimaryKeyConstraint('program_id', 'mentor_id', 'id', name='program_mentor_association_pkey')
    )
    op.create_index('ix_program_mentor_association_id', 'program_mentor_association', ['id'], unique=False)
    op.create_table('programs',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('avatar', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('mentor_manager_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('programs_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['mentor_manager_id'], ['mentor_managers.id'], name='programs_mentor_manager_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='programs_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_programs_id', 'programs', ['id'], unique=False)
    op.create_table('mentors',
    sa.Column('about', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('mentors_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='mentors_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='mentors_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_mentors_id', 'mentors', ['id'], unique=False)
    op.create_table('social_links',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='social_links_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='social_links_pkey')
    )
    op.create_table('roles',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('mentor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mentor_manager_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['mentor_id'], ['mentors.id'], name='roles_mentor_id_fkey'),
    sa.ForeignKeyConstraint(['mentor_manager_id'], ['mentor_managers.id'], name='roles_mentor_manager_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.create_index('ix_roles_id', 'roles', ['id'], unique=False)
    op.create_table('mentor_managers',
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('about', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('mentor_managers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='mentor_managers_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='mentor_managers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_mentor_managers_id', 'mentor_managers', ['id'], unique=False)
    op.create_table('locations',
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('profile_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], name='locations_profile_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='locations_pkey')
    )
    op.create_index('ix_locations_id', 'locations', ['id'], unique=False)
    op.create_table('users',
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.create_table('criteria',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('program_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], name='criteria_program_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='criteria_pkey')
    )
    op.create_index('ix_criteria_id', 'criteria', ['id'], unique=False)
    op.create_table('profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('profile_picture', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('about', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('website', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='profiles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='profiles_pkey')
    )
    # ### end Alembic commands ###
