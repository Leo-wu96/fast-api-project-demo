from fastapi import FastAPI, Depends
from typing import Optional


app = FastAPI()


class Common_Params():
    def __init__(self, q:Optional[str]=None, skip:int=0, limit:int=100):
        self.q = q
        self.skip = skip
        self.limit = limit
    
    
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/read_items")
async def read_items(common: Common_Params = Depends()):
    response = {}
    if common.q:
        response['q'] = common.q
    items = fake_items_db[common.skip, common.skip + common.limit]
    response['items'] = items
    
    return response

