'''
Author: zixian.wu@shopee.com
Date: 2024-04-18 14:31:19
LastEditTime: 2024-04-18 14:33:16
Description: file content
'''


from typing import Optional
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items")
async def read_items(user_agent:Optional[str] = Header(None)):
	return {"User_Agent": user_agent}