'''
Author: zixian.wu@shopee.com
Date: 2024-04-28 11:26:35
LastEditTime: 2024-04-28 11:53:42
Description: file content
'''
from fastapi import FastAPI, Depends, Cookie
from typing import Optional

app = FastAPI()

# 第一层依赖
def query_extractor(q: Optional[str]=None):
    return q


# 第二层依赖
# 注意，这里在路径操作函数中只声明了一个依赖项，即 query_or_cookie_extractor 。
# 但 FastAPI 必须先处理 query_extractor，以便在调用 query_or_cookie_extractor 时使用 query_extractor 返回的结果。
def query_cookie_extractor(q: str=Depends(query_extractor), last_query: Optional[str]=Cookie(None)):
    if q is not None:
        return q
    else:
        return last_query



# 第三层依赖
@app.get("/items/")
def get_items(q: str=Depends(query_cookie_extractor)):
    return {"q":q}


# 多次使用同一个依赖项
# 如果在同一个路径操作 多次声明了同一个依赖项，例如，多个依赖项共用一个子依赖项，FastAPI 在处理同一请求时，只调用一次该子依赖项。
# FastAPI 不会为同一个请求多次调用同一个依赖项，而是把依赖项的返回值进行「缓存」，并把它传递给同一请求中所有需要使用该返回值的「依赖项」。
# 在高级使用场景中，如果不想使用「缓存」值，而是为需要在同一请求的每一步操作（多次）中都实际调用依赖项，可以把 Depends 的参数 use_cache 的值设置为 False :
async def needy_dependency(fresh_value: str = Depends(query_cookie_extractor, use_cache=False)):
    return {"fresh_value": fresh_value}