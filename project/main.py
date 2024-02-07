from fastapi import FastAPI
from app.api.endpoints import crud

app = FastAPI()

app.include_router(crud.router)
