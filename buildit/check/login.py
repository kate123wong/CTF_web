import sys
sys.path.append("..")
import config
import requests
import hashlib,json


host = '127.0.0.1'
url_login = "http://" + host + ":5000/login"


session=""
username = "kate"
passwd = "123"
passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
data = {"username":username,"passwd":passwd}
try:
    res = requests.post(url=url_login,data=data)
    res = res.json()
    if( res["status"] == 206):
        session = res["session"]
        print(username, "登陆成功，你的session是：",res["session"])
except Exception:
    raise Exception
