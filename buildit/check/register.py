import sys
sys.path.append("..")
import config
import requests
import hashlib,json


host = config.host;
url = "http://"+host+":5000/register"
username = "test123"
passwd = "123"
passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
data = {"username":username,"passwd":passwd}
print(url,username,passwd)
res = requests.post(url=url,data=data)
res = res.text.json()
if res["status"] == 202:
    print(username,"注册成功,你的密码是：",passwd)
else:
    print("注册失败")

