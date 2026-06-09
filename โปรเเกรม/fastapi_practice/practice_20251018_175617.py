# Session: Weekend practice
# Note: This took a while to debug, but it works now.

from fastapi import FastAPI

# Source: FastAPI Official Docs
app = FastAPI()

# Path Parameters
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}