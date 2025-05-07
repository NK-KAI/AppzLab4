from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import Category


class Subcategory(Base):
    __tablename__ = 'subcategories'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    category_id: Mapped[list[int]] = mapped_column(ForeignKey('categories.id'))
    category: Mapped[list["Category"]] = relationship(back_populates='subcategories', lazy='subquery')
