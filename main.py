from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    tina = "tina"
    leo = "leo"
    shopee = "shopee"

class Item(BaseModel):
    name:str
    price:float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"hello": "world"}



@app.get("/items/{item_id}")
def read_items(item_id:int, q:Optional[str]=None):
    return {"item_id":item_id, "q":q}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"item_price": item.price, "item_id": item_id}


@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
    if model_name == ModelName.tina:
        return {"model_name": model_name, "message": "Good Girl!!!"}
    
    if model_name.value == 'leo':
        return {"model_name": model_name, "message": "Bad Boy!!!"}

    return {"model_name": model_name, "message": "BBGG!!!"}




#terminal: start up: uvicorn main:app --reload