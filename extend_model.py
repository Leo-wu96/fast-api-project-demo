'''
Author: zixian.wu@shopee.com
Date: 2024-04-19 16:13:26
LastEditTime: 2024-04-19 16:30:03
Description: file content
'''
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()



class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullName: Optional[str]=None
    
    
class UserIn(UserBase):
    password: str
    
    
class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hard_password: str
    

def hash_password(password):
    return "super_sensitive+" + password


