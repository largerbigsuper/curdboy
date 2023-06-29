
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import Base, engine
from routers import curdboy_router
from settings.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.APP_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.APP_ALLOW_METHODS,
    allow_headers=["*"],

)

app.include_router(curdboy_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)