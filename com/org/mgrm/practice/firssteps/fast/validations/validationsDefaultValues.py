from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

#use default values other than None
@app.get("/items/{item_id}")
async def read_items(q: Annotated[str, Query(min_length=3)]= "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# declare a value as required while using Query
@app.get("/items_required/{item_id}")
async def read_items_required(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#You can declare that a parameter can accept None, but that it's still required.
@app.get("/items_required_none/{item_id}")
async def read_items_none_required(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results