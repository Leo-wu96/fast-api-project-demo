'''
Author: zixian.wu@shopee.com
Date: 2024-04-26 18:54:12
LastEditTime: 2024-04-26 18:58:37
Description: file content
'''
from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()


async def common_parameters(q:Optional[str], skip:int=0, limit:int=100):
    return {"q":q, "skip":skip, "limit":limit}


@app.get("/items")
async def get_items(common:dict=Depends(common_parameters)):
    return common



@app.get("/users")
async def get_users(common:dict=Depends(common_parameters)):
    return common

# 接收到新的请求时，FastAPI 执行如下操作：

# 用正确的参数调用依赖项函数（「可依赖项」）
# 获取函数返回的结果
# 把函数返回的结果赋值给路径操作函数的参数


# 这样，只编写一次代码，FastAPI 就可以为多个路径操作共享这段代码。

# 注意，无需创建专门的类，并将之传递给 FastAPI 以进行「注册」或执行类似的操作。

# 只要把它传递给 Depends，FastAPI 就知道该如何执行后续操作。