from typing import List

from fastapi import APIRouter,  Depends,   status
from sqlalchemy.orm import Session

from dependencies import get_db, get_song_repo
from repositories.song_repository import SongRepo
from schemas.song_schemas import SongFull

router = APIRouter(
    prefix="/song",
    tags=["Songs"]
)


@router.get("/{id}", response_model=SongFull, status_code=status.HTTP_200_OK)
async def get_full_song(
    id:int,
    db: Session = Depends(get_db),
    song_repo: SongRepo = Depends(get_song_repo),
) -> SongFull:
    return await song_repo.get_full_song(id=id,db=db)