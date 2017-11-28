# -*- coding:utf-8 -*-


timedate = [31,28,31,30,31,30,31,31,30,31,30,31]
print("欢迎使用时间计算系统")
year = input("请输入年份：")
month = input("请输入月份：")
day = input("请输入日期：")
days = 0
if int(year) % 4 == 0 | int(year) % 400 == 0:
    timedate[1] = timedate[1] + 1
    for i in range(int(month)-1):
        days += timedate[i]
        days =days + int(day)
        print("你好，%s-%s-%s是%s年的第%s" % (year,month,day,year,days))
else:
    for i in range()