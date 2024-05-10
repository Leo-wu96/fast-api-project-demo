'''
Author: zixian.wu@shopee.com
Date: 2024-05-08 15:27:51
LastEditTime: 2024-05-10 10:42:05
Description: file content
'''
from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "hello world"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
