from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


class Manufacturer(BaseModel):
    name: str
    country: str

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    manufacturer: Manufacturer

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "offer": item.is_offer,
            "manufacturer": item.manufacturer.name, "manufacturer_country": item.manufacturer.country}

