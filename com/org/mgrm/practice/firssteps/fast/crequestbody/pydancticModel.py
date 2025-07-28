#To declare a request body, you use Pydantic models with all their power and benefits.
#To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel) :  #declare your data model as a class that inherits from BaseModel
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): #Declare it as a parameter
    
    return item