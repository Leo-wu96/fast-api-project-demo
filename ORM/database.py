'''
Author: zixian.wu@shopee.com
Date: 2024-05-07 11:51:22
LastEditTime: 2024-05-07 18:49:22
Description: file content
'''

# 导入sqlalchemy部分

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_ENGINE_URL = ""


engine = create_engine(SQLALCHEMY_ENGINE_URL)

# sessionmaker(autocommit=False, autoflush=False, bind=engine) 是 SQLAlchemy 库中的一个函数。它用于创建一个会话工厂，该工厂可以用来实例化会话对象。
# 这个函数的参数如下：
# autocommit=False：表示在会话中进行的操作不会自动提交到数据库。如果设置为True，则会话中的每个操作都会立即提交到数据库。
# autoflush=False：表示在会话中进行查询操作时，不会自动刷新（更新）会话中的对象状态。如果设置为 True，则会话中的每个查询操作都会自动刷新对象状态。
# bind=engine：表示要使用的数据库连接引擎。engine 是一个已经创建好的 SQLAlchemy 引擎对象，它可以用于连接数据库。
# 使用这个函数创建会话工厂后，可以通过调用工厂的 session()方法来创建会话对象，然后可以使用该对象执行数据库操作，如添加、修改、删除和查询等操作。创建的会话对象会绑定到指定的数据库引擎上，通过会话对象可以与数据库进行交互。

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


