
import datetime
import time
from typing import Optional

from fastapi import FastAPI
import student

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": time.time()}


@app.get("/stu")
def stu():
    data = ['1', '2']
    return {"q": data}


app.include_router(student.router)
