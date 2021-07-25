import sys
import requests
import hashlib,json
import requests

host = sys.argv[1]
port=sys.argv[2]
username = sys.argv[3]
passwd = sys.argv[4]

url_login = "http://" + host + ":"+port+ "/login"
url_reg= "http://"+host+":"+port+"/register"
password = hashlib.md5(passwd.encode('utf8')).hexdigest()
def login(url_login):
    try:
        session=""
        data = {"username":username,"passwd":password}
        try:
            res = requests.post(url=url_login,data=data)
            res = res.json()
            if( res["status"] == 206):
                session = res["session"]
                print(username, "登陆成功，你的session是：",res["session"])
            elif res["status"] == 205:
                print("密码错误，请稍后再试")
            elif res["status"] == 207:
                print("登录失败，请稍后再试")
            elif res["status"] == 210:
                print("内部错误，请稍后再试")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
        return False
    return True

def register(url_reg):
    try:
        password = hashlib.md5(passwd.encode('utf8')).hexdigest()
        data = {"username":username,"passwd":password}
        res = requests.post(url=url_reg,data=data)
        print(res)
        res = res.json()
        print(res)
        if res["status"] == 202:
            print(username,"注册成功,你的密码是：",passwd)
        elif res["status"] == 204:
            print("用户名已经注册，请更换用户名")
        elif res["status"] == 3:
            print("注册失败，请稍后再试")
        elif res["status"] == 210:
            print("内部错误，请稍后再试")
    except Exception as e:
        print(e)
        return False
    return True

def checker():
    try:
        if register(url_reg) and login(url_login):
            return (True,"IP: "+host+" OK")
    except Exception as e:
        return (False,"IP: "+host+" is down, "+str(e))

if __name__ == '__main__':
    print(checker())

