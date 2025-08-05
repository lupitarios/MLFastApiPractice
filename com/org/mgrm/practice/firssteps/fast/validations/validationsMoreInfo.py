#Declare more metadata .You can add more information about the parameter.
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

#You can add a title
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(title="Query string", min_length=3)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# And a description
@app.get("/items_desc/")
async def read_items(q: Annotated[str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        )] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Alias parameters
#you can declare an alias, and that alias is what will be used to find the parameter value
@app.get("/items_alias/")
async def read_items(q: Annotated[str | None, Query(alias="item-query-alias")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Deprecating parameters
# pass the parameter deprecated=True to Query
@app.get("/items_deprecated/")
async def read_items(q: Annotated[str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results