from config_db import SessionLocal
from repositories.album_repository import AlbumRepo
from repositories.singer_repository import SingerRepo
from repositories.song_repository import SongRepo

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_singer_repo():
    return SingerRepo()

def get_song_repo():
    return SongRepo()

def get_album_repo():
    return AlbumRepo()