'''
Author: zixian.wu@shopee.com
Date: 2024-04-28 18:05:15
LastEditTime: 2024-04-29 10:40:22
Description: file content
'''
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()




oAuth_schema = OAuth2PasswordBearer(tokenUrl='token')



# 这里tokenUrl="token"指的token是我们尚未创建的相对 URL 。因为它是一个相对 URL，所以它相当于./token.

# 因为我们使用的是相对 URL，如果您的 API 位于https://example.com/，那么它将引用https://example.com/token。但是如果您的 API 位于https://example.com/api/v1/，那么它将引用https://example.com/api/v1/token.

# 使用相对 URL 很重要，以确保您的应用程序即使在像Beyond a Proxy这样的高级用例中也能继续工作。

# 此参数不会创建该端点/路径操作，而是声明该 URL/token将是客户端应用于获取令牌的 URL 。该信息在 OpenAPI 中使用，然后在交互式 API 文档系统中使用。

# 我们很快也会创建实际的路径操作。

@app.get('/items')
async def get_items(token:str=Depends(oAuth_schema)):
    return {'token': token}


