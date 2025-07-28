#Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:

from fastapi import FastAPI

app = FastAPI()

@app.get( "/users/me" )
async def read_user_me() :
    return { "user_id" : "The current user" }

@app.get( "/users/{user_id}" )
async  def red_user(user_id : str) :
    return { "user_id" : user_id }

@app.get( "/users" )
async def read_users() :
    return [ "Rick", "Morty" ]

@app.get( "/users" )  #you cannot redefine a path operation
async def read_users2():
    return [ "Ben", "Elfo" ]