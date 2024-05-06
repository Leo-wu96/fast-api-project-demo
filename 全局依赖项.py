'''
Author: zixian.wu@shopee.com
Date: 2024-04-28 14:48:05
LastEditTime: 2024-04-28 14:53:08
Description: file content
'''
from fastapi import FastAPI, Depends, Header, HTTPException

# 有时，我们要为整个应用添加依赖项。
# 通过与定义路径装饰器依赖项 类似的方式，可以把依赖项添加至整个 FastAPI 应用。
# 这样一来，就可以为所有路径操作应用该依赖项


async def verify_token(token: str=Header()):
    if token != "1":
        raise HTTPException(status_code=400, detail="Invalid token")
    
    
async def verify_key(key: str=Header()):
    if key != "1":
        raise HTTPException(status_code=400, detail="Invalid key")
    return key

app = FastAPI(dependencies=[Depends(verify_key, verify_token)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]