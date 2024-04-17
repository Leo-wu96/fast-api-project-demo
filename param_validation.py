'''
Author: zixian.wu@shopee.com
Date: 2024-04-16 11:46:42
LastEditTime: 2024-04-16 17:11:19
Description: file content
'''
from fastapi import FastAPI, Query
from typing import Optional


app = FastAPI()



@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        alias = "item-query",
        deprecated = True
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
