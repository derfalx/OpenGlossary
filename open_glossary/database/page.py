from sqlalchemy.orm import Mapped, mapped_column

from open_glossary import db


class Page(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    content: Mapped[str]
