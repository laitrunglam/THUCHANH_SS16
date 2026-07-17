from module import *
from routes import RouterStudent
from fastapi import FastAPI
from database import *

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(RouterStudent)






