# the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.
from fastapi import FastAPI

app = FastAPI()

@app.get( "/files/{file_path:path}" )
async def read_file(file_path : str) :
    return {"file_path" : file_path}