from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.database import Base
from db.models import announcement_tag
from db.models import Announcement


class Tag(Base):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    announcements: Mapped[list['Announcement']] = relationship(back_populates="tags",
                                                               secondary=announcement_tag, lazy='subquery')
