from sqlalchemy import Column,  Integer, String 

from config_db import Base

class Singer(Base):
    __tablename__ = 'artists'

    artistid = Column(Integer, primary_key=True, index=True)
    name = Column(String)