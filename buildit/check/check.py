import sys
sys.path.append("..")
import config
import requests
import hashlib,json

host = sys.argv[1]
port=sys.argv[2]

url_login = "http://" + host + ":"+port+ "/login"
url_reg= "http://"+host+":"+port+"/register"

def login(url_login):
    try:
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
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    return True

def register(url_reg):
    try:
        username = "test123"
        passwd = "123"
        passwd = hashlib.md5(passwd.encode('utf8')).hexdigest()
        data = {"username":username,"passwd":passwd}
        print(url_reg,username,passwd)
        res = requests.post(url=url_reg,data=data)
        res = res.text.json()
        if res["status"] == 202:
            print(username,"注册成功,你的密码是：",passwd)
        else:
            print("注册失败")
    except Exception as e:
        print(e)
    return True

def checker():
    try:
        if register(url_reg) and login(url_login):
            return (True,"IP: "+host+" OK")
    except Exception as e:
        return (False,"IP: "+host+" is down, "+str(e))

if __name__ == '__main__':
    print(checker())

