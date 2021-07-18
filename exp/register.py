import sys
sys.path.append("..")
import config
import requests
import hashlib,json


host = config.host;
url = "http://"+host+":5000/register"
username = "kate"
passwd = "123"
passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
data = {"username":username,"passwd":passwd}
print(url,username,passwd)
res = requests.post(url=url,data=data)
print(res.text)

