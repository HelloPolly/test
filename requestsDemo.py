#!/usr/bin/env python3
# -*-coding:utf-8 -*-

#作者：HelloPolly
#时间：2017-12-6
#备注：演示requests

import requests
import json

#r=requests.get("http://www.baidu.com")
#print(r)
#print(r.status_code)
#print(r.headers)

#输入测试的接口地址
url = "https://postman-echo.com/post"
#输入测试输入
testdata="hello world!" 

 #输入headers
headers={
    'content-type':"text/plain"
}
#以POSt的方式进行请求，并把返回数据存到r这个变量中
r=requests.post(url,data=testdata,headers=headers) 

#把r的text的属性内容转换为json格式，并重新赋值给r
r=json.loads(r.text) 

#测试数据和返回数据做对比
if testdata == r["data"]:
    print("测试通过")
else:
    print("测试不通过")
    print(r["data"])