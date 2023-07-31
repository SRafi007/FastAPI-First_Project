from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/val/{param_Val}")
async def getParamVal(param_Val:int):
    return {"param":param_Val}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}