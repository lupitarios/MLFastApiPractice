#when you want to make a query parameter required, you can just not declare any default value
from fastapi import FastAPI

app = FastAPI()

@app.get( "/items/{item_id}" )
async def read_user_item( item_id : str, needey : str) :
    item = {"item_id" : item_id, "needy" : needey}
    return item