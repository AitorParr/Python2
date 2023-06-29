from pydantic import BaseModel


class SingerModel(BaseModel):
    artistid: int | None
    name: str | None


# usado para entregar un cantante
class SingerInDB(SingerModel):
    artistid: int
    name: str

    class Config:
        orm_mode = True