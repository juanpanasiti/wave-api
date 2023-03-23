from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import api_router
from app.database.wave_db import wave_db
from app.database.product_model import ProductModel


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(api_router)

@app.on_event('startup')
def on_startup():
    try:
        wave_db.db.connect()
    except Exception as ex:
        print(ex.args)


