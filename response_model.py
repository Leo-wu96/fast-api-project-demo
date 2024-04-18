'''
Author: zixian.wu@shopee.com
Date: 2024-04-18 15:39:21
LastEditTime: 2024-04-18 18:52:47
Description: file content
'''
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, List


app = FastAPI()

# 明文输入密码
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str]=None
    

# 隐藏输出密码
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str]=None
    
@app.get("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user




class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: float=0.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# response_model_exclude_unset: 从结果中忽略它们的默认值
@app.get("/items/", response_model=Item, response_model_exclude_unset=True)
async def read_items(item_id: str):
    return items[item_id]