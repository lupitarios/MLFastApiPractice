from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

#Exclude parameters from OpenAPI. set the parameter include_in_schema of Query to False
@app.get("/items/")
async def read_items(hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}