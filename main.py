from fastapi import FastAPI
from api.endpoints import __routers__
from db.database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

for router in __routers__:
    app.include_router(router)


