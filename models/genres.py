from sqlalchemy import Column,  Integer, String

from config_db import Base

class Genres(Base):
    __tablename__ = 'genres'

    genreid = Column(Integer, primary_key=True, index=True)
    name = Column(String)