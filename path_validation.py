'''
Author: zixian.wu@shopee.com
Date: 2024-04-16 17:12:16
LastEditTime: 2024-04-17 09:44:15
Description: file content
'''
from typing import Optional
from fastapi import FastAPI, Path, Query


app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(q: str, item_id):
    pass