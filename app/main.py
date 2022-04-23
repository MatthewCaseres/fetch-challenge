from fastapi import FastAPI
from pydantic import BaseModel
from .grid import getOpposingCorners, getGrid

class Input(BaseModel):
    dims: list[int]
    rectangle: list[list[float]]

app = FastAPI()

@app.post("/calculate/")
async def create_item(input: Input):
    topLeft, bottomRight = getOpposingCorners(input.rectangle)
    grid = getGrid(input.dims, topLeft, bottomRight)
    # must be JSON serializable
    return grid.tolist()

@app.get("/")
def read_root():
    return {"Hello": "World"}