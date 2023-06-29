from pydantic import BaseModel


class AlbumModel(BaseModel):
    albumid :int | None
    title: str | None
    artistid: int | None
    


# usado para entregar un cantante
class AlbumInDB(AlbumModel):
    albumid :int 
    title: str 
    artistid: int 

    class Config:
        orm_mode = True