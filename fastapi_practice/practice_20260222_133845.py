# Session: Weekend practice
# Note: Awesome feature.

from fastapi import FastAPI
from pydantic import BaseModel

# Source: FastAPI Official Docs - Request Body
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

@app.post('/items/')
def create_item(item: Item):
    return item