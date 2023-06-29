from typing import List

from fastapi import APIRouter,  Depends,   status
from sqlalchemy.orm import Session

from dependencies import get_singer_repo, get_db,get_album_repo
from repositories.album_repository import AlbumRepo
from repositories.singer_repository import SingerRepo
from schemas.albums_schemas import AlbumInDB
from schemas.singer_schemas import SingerInDB

router = APIRouter(
    prefix="/singers",
    tags=["Singer"]
)


@router.get("/", response_model=List[SingerInDB], status_code=status.HTTP_200_OK)
async def get_all_singers(
    db: Session = Depends(get_db),
    singer_repo: SingerRepo = Depends(get_singer_repo),
) -> List[SingerInDB] :
    return await singer_repo.get_all_singers(db=db)

@router.get("/{id}", response_model=List[AlbumInDB], status_code=status.HTTP_200_OK)
async def get_album_singer(
    id:int,
    db: Session = Depends(get_db),
    album_repo: AlbumRepo = Depends(get_album_repo),
) -> List[AlbumInDB]:
    return await album_repo.get_album_singer(id=id,db=db)