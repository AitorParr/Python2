from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from controllers.singer_routes import router as singer_router
from controllers.songA_routes import router as song_router
from controllers.songs_routes import router as songs_router
from controllers.albums_routes import router as albums_router

def get_application():

    # crea la base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Chinnok", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(singer_router, prefix="/api/v1")
    app.include_router(song_router, prefix="/api/v1")
    app.include_router(songs_router, prefix="/api/v1")
    app.include_router(albums_router, prefix="/api/v1")
    return app

app = get_application()

@app.get("/")
def home() -> dict:
    return {"mensaje": "Bienvenido a chinook"}