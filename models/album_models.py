from sqlalchemy import Column,  Integer, String, ForeignKey

from config_db import Base

class Album(Base):
    __tablename__ = 'albums'

    albumid = Column(Integer, primary_key=True, index=True)
    artistid = Column(Integer, ForeignKey("artists.artistid"))
    title = Column(String)