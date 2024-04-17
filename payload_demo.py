from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float]=None
    
    
app = FastAPI()


@app.post("/item")
async def create(item:Item):
    return item



@app.post("/item/key_item")
async def create_key(item: Item = Body(..., embed = True)):
    return item

