'''
Author: zixian.wu@shopee.com
Date: 2024-05-08 10:39:16
LastEditTime: 2024-05-08 11:25:31
Description: file content
'''
from sqlalchemy import Boolean, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    # 该__tablename__属性告诉 SQLAlchemy 在数据库中为这些模型中的每一个使用的表的名称
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    items = relationship("Item", back_populates="owner")
    

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="items")

