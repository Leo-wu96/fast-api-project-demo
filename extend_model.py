'''
Author: zixian.wu@shopee.com
Date: 2024-04-19 16:13:26
LastEditTime: 2024-04-22 14:05:24
Description: file content
'''
from typing import Union, Optional, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()



class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullName: Optional[str]=None
    
    
class UserIn(UserBase):
    password: str
    
    
class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hard_password: str
    

def hash_password(password):
    return "super_sensitive+" + password

# 关于 **user_in.dict()
# Pydantic 的 .dict()
# user_in 是一个 UserIn 类的 Pydantic 模型.

# Pydantic 模型具有 .dict（） 方法，该方法返回一个拥有模型数据的 dict, 已弃用，改用.model_dump
# 因此，如果我们像下面这样创建一个 Pydantic 对象 user_in：

# user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
# 然后我们调用：

# user_dict = user_in.dict()
# 现在我们有了一个数据位于变量 user_dict 中的 dict（它是一个 dict 而不是 Pydantic 模型对象）。

# 如果我们调用：

# print(user_dict)
# 我们将获得一个这样的 Python dict：

# {
#     'username': 'john',
#     'password': 'secret',
#     'email': 'john.doe@example.com',
#     'full_name': None,
# }


def fake_user_save(userin: UserIn):
    fake_password = hash_password(userin.password)
    userinDB = UserInDB(**userin.model_dump(), hard_password=fake_password)
    return userinDB



@app.post("/create_user/", response_model=UserOut)
async def create_user(userin: UserIn):
    userinDB = create_user(userin)
    return userinDB


 
###### Union or anyOf 的用法，可以设置不同的模型响应 #########
class BaseItem(BaseModel):
    description: str
    type: str
    

class CarItem(BaseItem):
    type = "car"


class PlantItem(BaseItem):
    type = "plant"
    size: int
    
items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@app.get("/items/", response_model=Union[CarItem, PlantItem])
async def get_items(item_id: str):
    return items[item_id]



### 由对象列表构成的响应 ######
class Item():
    name:str
    description:str

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get("/items/", response_model=List(Item))
async def get_items1():
    return items
    
    
### 由任意dict构成的响应#####
# 你还可以使用一个任意的普通 dict 声明响应，仅声明键和值的类型，而不使用 Pydantic 模型。

# 如果你事先不知道有效的字段/属性名称（对于 Pydantic 模型是必需的），这将很有用。

# 在这种情况下，你可以使用 typing.Dict
@app.get("/items/", response_model=Dict[str, float])
async def get_items2():
    return {"1":1, "2": 2}

