from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

from config_db import Base

class Song(Base):
    __tablename__ = 'tracks'

    trackid = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    albumid = Column(Integer,ForeignKey("albums.albumid"))
    mediatypeid = Column(Integer,ForeignKey("media_types.mediaTypeid"))
    genreid = Column(Integer,ForeignKey("genres.genreid"))
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unitprice= Column(Numeric)


