from typing import List

from sqlalchemy.orm import Session

from models.singer_models import Singer
from schemas.singer_schemas import  SingerInDB

class SingerRepo:

    # obtiene todos los cantantes
    async def get_all_singers(self, db: Session) -> List[SingerInDB]:
        singer_list: List[SingerInDB] = db.query(Singer).all()
        print(singer_list)
        return singer_list
    
