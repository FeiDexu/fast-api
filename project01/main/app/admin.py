from fastapi import FastAPI

app = FastAPI()

@app.get("qq/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": datetime.datetime.now()}


# @app.get("/stu")
# def stu():
#     data = ['1', '2']
#     return {"q": data}
