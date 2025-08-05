from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getHelloWorld():
    return { "message" : "Hello World "}

@app.get("/helloWorld2")
async def getHelloWorld2():
    return { "message" : "Hello World2 "}



