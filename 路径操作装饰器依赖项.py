'''
Author: zixian.wu@shopee.com
Date: 2024-04-28 14:30:53
LastEditTime: 2024-04-28 14:44:22
Description: file content
'''
from fastapi import FastAPI, Depends, Header, HTTPException


app = FastAPI()

# 路径操作装饰器依赖项（以下简称为“路径装饰器依赖项”）的执行或解析方式和普通依赖项一样，但就算这些依赖项会返回值，它们的值也不会传递给路径操作函数。

# 有些编辑器会检查代码中没使用过的函数参数，并显示错误提示。

# 在路径操作装饰器中使用 dependencies 参数，可以确保在执行依赖项的同时，避免编辑器显示错误提示。

# 使用路径装饰器依赖项还可以避免开发新人误会代码中包含无用的未使用参数。


async def check_token(value:str=Header()):
    if value != "1":
        raise HTTPException(status_code=400, detail="Invalid token!")


async def check_value(value:str=Header()):
    if value != "1":
        # 路径装饰器依赖项与正常的依赖项一样，可以 raise 异常
        raise HTTPException(status_code=400, detail="Invalid value!")
    return value


@app.get("/items/", dependencies=[Depends(check_token), Depends(check_value)])
async def get_items():
    return 1


