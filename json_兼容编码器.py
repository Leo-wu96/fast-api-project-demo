'''
Author: zixian.wu@shopee.com
Date: 2024-04-26 18:28:46
LastEditTime: 2024-04-26 18:37:01
Description: file content
'''
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name:str
    time:datetime
    description:Optional[str]=None
    
fake_db = {}


@app.put("/items/{id}")
async def update_item(id:str, item:Item):
    json_compat_data = jsonable_encoder(item)
    fake_db[id] = json_compat_data
    

# 在此示例中，它将 Pydantic 模型转换为一个字典，并将这个datetime转换为一个字符串。

# 调用它的结果是可以用 Python 标准编码的东西json.dumps()。

# 它不会str以 JSON 格式（作为字符串）返回包含数据的大文件。它返回一个 Python 标准数据结构（例如 a dict)，其值和子值都与 JSON 兼容