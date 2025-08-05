#When you define a query parameter explicitly with Query you can also declare it to receive a list of values,
# or said in another way, to receive multiple values.
# ** Query parameter list / multiple values ***

from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()]):
    query_item = {"q" : q}
    return query_item

#http://localhost:8000/items/?q=foo&q=bar

# *** Query parameter list / multiple values with defaults ***
@app.get("/items_default/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

# **** Using just list
# list[int] would check (and document) that the contents of the list are integers. But list alone wouldn't.
@app.get("/items_list/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items