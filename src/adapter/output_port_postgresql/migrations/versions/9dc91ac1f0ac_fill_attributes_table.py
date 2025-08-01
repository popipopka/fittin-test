"""fill attributes table

Revision ID: 9dc91ac1f0ac
Revises: e3a2942f37cd
Create Date: 2025-08-01 18:35:26.152382

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9dc91ac1f0ac'
down_revision: Union[str, Sequence[str], None] = 'e3a2942f37cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.bulk_insert(
        sa.table(
            'attributes',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String(length=32)),
        ),
        [
            {'id': 1, 'name': 'Тип меха'},
            {'id': 2, 'name': 'Цвет'},
            {'id': 3, 'name': 'Размер'},
            {'id': 4, 'name': 'Длина изделия'},
            {'id': 5, 'name': 'Сезон'},
            {'id': 6, 'name': 'Страна производства'},
            {'id': 7, 'name': 'Застежка'},
            {'id': 8, 'name': 'Подкладка'},
            {'id': 9, 'name': 'Стиль'},
            {'id': 10, 'name': 'Капюшон'},
            {'id': 11, 'name': 'Рукав'},
            {'id': 12, 'name': 'Воротник'},
            {'id': 13, 'name': 'Коллекция'},
            {'id': 14, 'name': 'Пол'},
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('truncate table attributes restart identity cascade')
