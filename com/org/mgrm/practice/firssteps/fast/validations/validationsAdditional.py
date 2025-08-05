from fastapi import FastAPI, Query
from typing import Annotated  # To declare generic types / part of type hints

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None,
Query(min_length=3,
      max_length=50,
      pattern="^fixedquery$")]
                     = None): #its length doesn't exceed 50 characters.
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
    return results