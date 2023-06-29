from sqlalchemy import Column,  Integer, String

from config_db import Base

class Mediatype(Base):
    __tablename__ = 'media_types'

    mediatypeid = Column(Integer, primary_key=True, index=True)
    name = Column(String)