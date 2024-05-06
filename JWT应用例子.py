'''
Author: zixian.wu@shopee.com
Date: 2024-04-30 14:29:05
LastEditTime: 2024-05-06 11:42:32
Description: file content
'''
from fastapi import FastAPI, HTTPException, Depends, status
from typing import Optional
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()


# 处理JWT令牌
# 创建一个随机密钥，该密钥将用于对 JWT 令牌进行签名。
# 要生成一个安全的随机密钥，可使用以下命令
# openssl rand -hex 32
# 然后将输出复制到变量 「SECRET_KEY」 中（不要使用示例中的这个）。

# 创建用于设定 JWT 令牌签名算法的变量 「ALGORITHM」，并将其设置为 "HS256"。

# 创建一个设置令牌过期时间的变量。

# 定义一个将在令牌端点中用于响应的 Pydantic 模型。

# 创建一个生成新的访问令牌的工具函数

SECRET_KEY = "fa469ead1cb7dd42a4ae97a94707414f10c0fe9f9048e162889cfadb081dcf20"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    username: Optional[str]=None
    

class User(BaseModel):
    username: str
    email: Optional[str]=None
    full_name: Optional[str]=None
    disabled: Optional[bool]=None


class UserInDB(User):
    hashed_password: str


app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hash_password):
    pwd_context.verify(plain_password, hash_password)



def hash_password(password):
    pwd_context.hash(password)
    

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)



def authenticate(fake_db, username:str, password:str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not password:
        return False
    
    return user

def create_access_token(data:dict, expire_time_delta:Optional[timedelta]=None):
    to_encode = data.copy()
    if expire_time_delta:
        expire_time = datetime.now() + expire_time_delta
    else:
        expire_time = datetime.now() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire_time})
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return token


    
async def get_current_user(token: str=Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(user:User=Depends(get_current_user)):
    if user.disabled:
        raise HTTPException(status_code=401, detail="Invalid user")
    
    return user


@app.post("/token/", response_model=TokenData)
async def login_for_access_token(formdata:OAuth2PasswordRequestForm=Depends()):
    user = authenticate(fake_users_db, formdata.username, formdata.password)
    if not user:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(data={"sub": user.username}, expire_time_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/users/me/", response_model=User)
async def read_users_me(current_user:User=Depends(get_current_active_user())):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]