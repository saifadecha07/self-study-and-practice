# Session: Weekend practice
# Note: Need to memorize this syntax.

from fastapi import FastAPI

# Source: FastAPI Official Docs
app = FastAPI()

# Path Parameters
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}