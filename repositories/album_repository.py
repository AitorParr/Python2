from typing import List

from sqlalchemy.orm import Session

from models.album_models import Album
from schemas.albums_schemas import  AlbumInDB

class AlbumRepo:

    # obtiene todos los cantantes
    async def get_album_singer(self, db: Session, id:int) -> List[AlbumInDB]:
        album_list: List[AlbumInDB] = db.query(Album).filter_by(artistid=id).all()
        return album_list
    