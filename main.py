from fastapi import FastAPI
from api.endpoints import __routers__
from db.models import (announcement,
                       announcement_tag,
                       category,
                       tag,
                       user,
                       subcategory)
from db.database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

for router in __routers__:
    app.include_router(router)


