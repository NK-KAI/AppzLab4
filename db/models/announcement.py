from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.database import Base
from db.models.announcement_tag import announcement_tag

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models import User, Tag
    from db.models.category import Category


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # M:1
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped[Optional["Category"]] = relationship(back_populates="announcements", lazy='subquery')

    # M:1
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[Optional["User"]] = relationship(back_populates="announcements", lazy='subquery')

    # M:N
    tags: Mapped[list["Tag"]] = relationship(secondary=announcement_tag, lazy='subquery')
