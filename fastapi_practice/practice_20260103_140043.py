# Session: Late night coding
# Note: Finally understood this concept!

from fastapi import FastAPI, Query

# Source: FastAPI Official Docs - Query Parameters
app = FastAPI()

@app.get('/items/')
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results