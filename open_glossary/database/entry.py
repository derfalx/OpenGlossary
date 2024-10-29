from typing import List

from sqlalchemy.types import JSON
from sqlalchemy.orm import Mapped, mapped_column

from open_glossary import db


class GlossaryEntry(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    letter: Mapped[str]
    meta: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
