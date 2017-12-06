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

url = "https://postman-echo.com/post" #输入测试的接口地址
testdata="hello world!"#输入测试输入
headers={ #输入headers
    'content-type':"text/plain"
}
r=requests.post(url,data=testdata,headers=headers)#以POSt的方式进行请求，并把返回数据存到r这个变量中
r=json.loads(r.text)#把r的text的属性内容转换为json格式，并重新赋值给r
if testdata == r["data"]:#测试数据和返回数据做对比
    print("测试通过")
else:
    print("测试不通过")
    print(r["data"])