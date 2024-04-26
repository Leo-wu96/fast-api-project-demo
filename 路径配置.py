'''
Author: zixian.wu@shopee.com
Date: 2024-04-25 18:53:43
LastEditTime: 2024-04-26 10:15:24
Description: file content
'''
from fastapi import FastAPI, status
from typing import Optional, Set
from pydantic import BaseModel



app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[str]=None
    tags: Set[str]=None


# 响应码的配置
@app.post('/items/', response_model = Item, status_code=status.HTTP_201_CREATED, summary="Create a new item")
async def create_model(item:Item):
    return item


# controller 标签
@app.get("/items", tags=['items'])
async def read_item():
    return [{"Name": "foo", "price": 42}]


@app.get("/users/", tags=[['user']])
async def read_user():
    return [{"Name": "foo"}]




