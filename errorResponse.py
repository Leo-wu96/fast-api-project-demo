'''
Author: zixian.wu@shopee.com
Date: 2024-04-24 17:50:21
LastEditTime: 2024-04-25 10:38:56
Description: file content
'''
from fastapi import FastAPI, HTTPException


app = FastAPI()


item = {}
@app.get("/item/{item_id}")
async def get_item(item_id:str):
    if item_id not in item:
        raise HTTPException(status_code=404, detail="item not found")
    return item[item_id]




### 添加自定义响应头
@app.get("/item1/{item_id}")
async def get_item1(item_id:str):
    if item_id not in item:
        raise HTTPException(status_code=404, detail="item not found", headers={"X-ERROR": "There goes my error"})
    return item[item_id]



#### 自定义异常响应
# 定义UnicornException, 在read_unicorn中抛出exception，而这个exception会被fastapi全局捕捉到，即通过exception_handler捕捉，然后对这个exception进行加工处理
from fastapi import Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name:str):
        self.name = name
        

@app.exception_handler(UnicornException)
async def exception_handler(request:Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name:str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {'unicorn_name': name}


