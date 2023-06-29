from pydantic import BaseModel


class SongModel(BaseModel):
    trackid: int 
    name: str | None
    albumid: int | None
    mediatypeid:int | None
    genreid:int | None
    composer:str | None
    milliseconds:int | None
    bytes:int | None
    unitprice:float | None


# usado para entregar un cantante
class SongInDB(SongModel):
    trackid: int
    name: str
    albumid: int
    mediatypeid:int
    genreid:int
    milliseconds:int
    bytes:int
    unitprice:float

    class Config:
        orm_mode = True

class SongFull(SongModel):
    trackid: int
    name: str
    albumid: int
    milliseconds:int
    bytes:int
    unitprice:float
    media_type_name:str
    genres_name:str


