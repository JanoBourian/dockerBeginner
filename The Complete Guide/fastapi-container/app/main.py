from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "hello!"}

@app.get("/item/{item_id}")
async def item(item_id:str):
    return {"item": f"{item_id}"}

@app.get("/user/{user_id}")
async def user(user_id:str):
    return {"user": f"{user_id}"}