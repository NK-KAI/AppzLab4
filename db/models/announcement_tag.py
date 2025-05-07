from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from db.database import Base

announcement_tag = Table(
    'announcement_tags',
    Base.metadata,
    Column('announcement_id', ForeignKey('announcements.id')),
    Column('tag_id', ForeignKey('tags.id'))
)
