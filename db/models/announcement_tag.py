from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from db.database import Base

advertisement_tag = Table(
    'advertisement_tag', Base.metadata,
    Column('advertisement_id', ForeignKey('advertisements.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True))
