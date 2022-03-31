"""create notes table

Revision ID: 97bfee197b16
Revises: 
Create Date: 2022-03-31 20:54:07.064740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97bfee197b16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table(
		"notes",
		sa.Column("id", sa.Integer, primary_key=True),
		sa.Column("text", sa.String),
		sa.Column("completed", sa.Boolean)
	)


def downgrade():
	op.drop_table("notes")
