'''
Author: zixian.wu@shopee.com
Date: 2024-04-18 12:02:42
LastEditTime: 2024-04-18 12:08:00
Description: file content
'''
from typing import Optional
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(ads_item: Optional[str] = Cookie(None)):
    return ads_item