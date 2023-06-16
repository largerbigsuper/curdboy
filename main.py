
import uvicorn
from fastapi import FastAPI
from routers import curdboy_router
from apps.users import models
from database.db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(curdboy_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)