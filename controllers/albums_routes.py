from typing import List

from fastapi import APIRouter,  Depends,   status
from sqlalchemy.orm import Session

from dependencies import get_db, get_song_repo
from repositories.song_repository import SongRepo
from schemas.song_schemas import SongInDB

router = APIRouter(
    prefix="/singer",
    tags=["Singer"]
)


@router.get("/{id}", response_model=List[SongInDB], status_code=status.HTTP_200_OK)
async def get_songs_artist(
    id:int,
    db: Session = Depends(get_db),
    song_repo: SongRepo = Depends(get_song_repo),
) -> List[SongInDB]:
    return await song_repo.get_songs_artist(id=id,db=db)
