# Session: Late night coding
# Note: This took a while to debug, but it works now.

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