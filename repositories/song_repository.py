from typing import List

from sqlalchemy.orm import Session
from models.album_models import Album
from models.media_type_models import Mediatype
from models.genres import Genres
from models.song_models import Song
from schemas.song_schemas import  SongInDB,SongFull

class SongRepo:

    # obtiene las canciones de un album
    async def get_songs_album(self, db: Session,id:int) -> List[SongInDB]:
        song_list: List[SongInDB] = db.query(Song).filter_by(albumid=id).all()
        return song_list
    
    # obtiene las canciones de un artista
    async def get_songs_artist(self, db: Session, id:int) -> List[SongInDB]:
        song_list: List[SongInDB] = db.query(Song).join(Album).filter_by(artistid=id).all()
        return song_list
    
    # obtiene las canciones en full
    async def get_full_song(self, db: Session, id:int) -> SongFull:
        song_list: SongFull = db.query(Song.trackid,
                                       Song.name,
                                       Song.albumid,
                                       Song.mediatypeid,
                                       Song.genreid,
                                       Song.composer,
                                       Song.milliseconds,
                                       Song.bytes,
                                       Song.unitprice,
                                       Mediatype.name,
                                       Genres.name).filter_by(trackid=id).join(Mediatype,Song.mediatypeid==Mediatype.mediatypeid).join(Genres,Song.genreid==Genres.genreid).all()
        kw = ['trackid','name','albumid','mediatypeid','genreid','composer','milliseconds','bytes','unitprice','media_type_name','genres_name']
        song_list = dict(zip(kw,*song_list))
        return song_list
    
