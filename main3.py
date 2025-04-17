from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

    class Config:
        alias_generator = lambda string: string.upper()
        allow_population_by_field_name = True


@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "offer": item.is_offer}

