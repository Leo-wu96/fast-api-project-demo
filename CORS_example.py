'''
Author: zixian.wu@shopee.com
Date: 2024-05-06 16:27:15
LastEditTime: 2024-05-06 18:24:39
Description: file content
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origin = [
    "http://localhost.taobao.com",
    "https://localhost.taobao.com",
    "http://localhost",
    "http://localhost:8080",    
]

app.middleware(
    CORSMiddleware,
    allow_origin=origin,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

# 默认情况下，这个 CORSMiddleware 实现所使用的默认参数较为保守，所以你需要显式地启用特定的源、方法或者 headers，以便浏览器能够在跨域上下文中使用它们。

# 支持以下参数：

# allow_origins - 一个允许跨域请求的源列表。例如 ['https://example.org', 'https://www.example.org']。你可以使用 ['*'] 允许任何源。
# allow_origin_regex - 一个正则表达式字符串，匹配的源允许跨域请求。例如 'https://.*\.example\.org'。
# allow_methods - 一个允许跨域请求的 HTTP 方法列表。默认为 ['GET']。你可以使用 ['*'] 来允许所有标准方法。
# allow_headers - 一个允许跨域请求的 HTTP 请求头列表。默认为 []。你可以使用 ['*'] 允许所有的请求头。Accept、Accept-Language、Content-Language 以及 Content-Type 请求头总是允许 CORS 请求。
# allow_credentials - 指示跨域请求支持 cookies。默认是 False。另外，允许凭证时 allow_origins 不能设定为 ['*']，必须指定源。
# expose_headers - 指示可以被浏览器访问的响应头。默认为 []。
# max_age - 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600。
# 中间件响应两种特定类型的 HTTP 请求……


@app.get("/")
async def main():
    return {"message": "Hello World!"}

