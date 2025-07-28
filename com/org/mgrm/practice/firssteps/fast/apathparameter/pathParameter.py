from fastapi import FastAPI

app = FastAPI()

@app.get("/parameters/no_type/{items_id}")
async def read_item_notype(item_id) :
    return { "item_id": item_id}

@app.get("/parameters/type/{items_id}")
async def read_item_notype(item_id : int) :
    return { "item_id": item_id}