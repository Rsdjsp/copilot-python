
app = FastAPI()

@app.post("/json")
async def json_endpoint(payload: dict):
    return {"payload": payload}
from fastapi import FastAPI

