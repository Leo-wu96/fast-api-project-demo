'''
Author: zixian.wu@shopee.com
Date: 2024-04-24 09:50:21
LastEditTime: 2024-04-24 10:07:56
Description: file content
'''
from fastapi import FastAPI, File, UploadFile

app = FastAPI()



@app.post("/create_file/")
async def create_file(file:bytes=File()):
    return {"file_size": len(file)}


# File 是直接继承自 Form 的类。

# 注意，从 fastapi 导入的 Query、Path、File 等项，实际上是返回特定类的函数。

# 提示

# 声明文件体必须使用 File，否则，FastAPI 会把该参数当作查询参数或请求体（JSON）参数。

# 文件作为「表单数据」上传。

# 如果把路径操作函数参数的类型声明为 bytes，FastAPI 将以 bytes 形式读取和接收文件内容。

# 这种方式把文件的所有内容都存储在内存里，适用于小型文件。

# 不过，很多情况下，UploadFile 更好用。



@app.post("/create_upload_file/")
async def create_upload_file(file:UploadFile=File()):
    return {"file_name": file.filename}


