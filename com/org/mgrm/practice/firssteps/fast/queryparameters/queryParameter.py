#The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
#Exemple http://127.0.0.1:8000/items/?skip=0&limit=10 -- Default value

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]

@app.get("/items/")
async def read_item( skip: int = 0, limit: int = 10) :  #skip parameter 1, limit parameter 2
    return fake_items_db[skip : skip + limit]