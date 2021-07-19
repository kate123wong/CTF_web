from flask import Flask,render_template, request
from hashlib import md5
import requests
import pymysql,threading
import base64
import json
import time
import random
import os

lock=threading.Lock()
<<<<<<< HEAD:web/hello.py
conn=pymysql.connect(host = '192.168.0.158' # 连接名称，默认127.0.0.1
=======
conn=pymysql.connect(host = "composemysql" # 连接名称，默认127.0.0.1
>>>>>>> 684dd5bca7b091b2f584ef783115745d1f7e0234:docker/fakebook/hello.py
,user = 'root' # 用户名
,passwd='6iuVhYwmxC' # 密码
,port= 3306 # 端口，默认为3306
,db='socialcontact' # 数据库名称
,charset='utf8' # 字符编码
)


app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/friends',methods=['POST'])
def getFriends():
    sql="select username from Users"
    data=tuple()
    cur = conn.cursor()
    try:
        lock.acquire()
        cur.execute(sql) # 执行查询的sql语句
        lock.release()
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except:
        conn.rollback()# 如果发生错误则回滚
    dic ={}
    while True:
        id = (int)(random.random() * 10 + 1)
        if id < len(data):
            name = data[id][0]
            dic[id]=name
            if(len(dic) == 6):
                break
    friends={}
    i = 1
    for key in dic.keys():
        friends["username"+str(i)] = dic[key];
        i = i + 1
    status = 208
    return json.dumps({"status":status,"friends":friends})

@app.route('/login',methods=['GET'])
def tologin():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():

    status = 210
    #获取登陆的用户名和密码
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    
    #在数据库中查询该用户名是否注册已经密码是否正确
    sql="select * from Users where username = %s"
    params = (username)
    try:
        cur = conn.cursor()
        cur.execute(sql,params) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except:
        conn.rollback()# 如果发生错误则回滚
    if len(data) == 1:
        #只要用户已经注册并且密码正确，就重新生成session值，不管现在是否是登陆状态。
        if data[0][2] == passwd:
            if data[0][1] == "admin":
                if data[0][3] != None:
                    session = data[0][3]
                    status = 206
                    return json.dumps({ 'status': status, 'session' : session})
            session = md5((str(time.time()) + str(random.random()) ).encode('utf8')).hexdigest()
            sql_set_session = "update Users set session= %s where username= %s and 3passwd2= %s"
            params_set_session = (session,username,passwd)
            try:
                cur.execute(sql_set_session,params_set_session)
                conn.commit()
                status = 206 # 成功登陆
                cur.close()
                return json.dumps({ 'status': status, 'session' : session})
            except Exception as e:
                conn.rollback()
                status = 207 #登陆失败
                cur.close()
        else:
            status = 205
    else:
        # print("username",username,"has not  registered!")
        # return render_template('register.html')
        #html = render_template('register.html')
        status = 201
    cur.close()
    return json.dumps({ 'status': status})

@app.route('/register',methods=['GET'])
def toregister():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register():
    status = 210 #其他状态
    #获取注册的用户名和密码
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    
    #在数据库中查询该用户名是否已经被注册
    sql="select * from Users where username = %s"
    params = (username)
    data = tuple()
    lock.acquire()
    try:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(sql,params) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
        cur.close()
    except:
        conn.rollback()# 如果发生错误则回滚
    lock.release()
    #the username haven't been registered
    if len(data) == 0:
        regist = 'insert into Users (username,3passwd2) values (%s, %s)'
        params_regist = (username,passwd)
        try:
            cur=conn.cursor()
            cur.execute(regist,params_regist)
            conn.commit()
            status = 202 #注册成功
        except:
            conn.rollback()
            status = 203 #注册失败
    else:
        status = 204 #用户已被注册
    return json.dumps({'status': status})

@app.route('/index',methods=['GET'])
def toIndex():
    status = 210
    username = request.args.get('username')
    passwd = request.args.get('passwd')
    session = request.args.get('session')
    cur = conn.cursor()
    sql="select * from Users where username = %s and 3passwd2 = %s and session = %s"
    params = (username,passwd,session)
    try:
        cur.execute(sql,params)
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except Exception as e:
        conn.rollback()# 如果发生错误则回滚

        #the username has been registered,he can login in.
    if len(data) == 1:
        return render_template('/index.html')
     # user hasn't been registered, or passwd is wrong or he doesn't login in.
    return "You have not login in."


@app.route('/index',methods=['POST'])
def TODO_toUserindex():

    status = 210
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    session = request.form.get('session')
    
    cur = conn.cursor()
    sql="select * from Users where username = %s and 3passwd2 = %s and session = %s"
    params = (username,passwd,session)
    try:
        cur.execute(sql,params)
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except Exception as e:
        conn.rollback()# 如果发生错误则回滚

        #the username has been registered,he can login in.
    if len(data) == 1:
        status = 208
        html = render_template('index.html')
        return json.dumps({"status" : status, "html" : html})
     # user hasn't been registered, or passwd is wrong or he doesn't login in.
    return json.dumps({"status" : 207})

@app.route('/user',methods=['GET'])
def toUserIndex():
    status = 210
    username = request.args.get('username')
    passwd = request.args.get('passwd')
    session = request.args.get('session')
    cur = conn.cursor()
    sql="select * from Users where username = %s and 3passwd2 = %s and session = %s"
    params = (username,passwd,session)
    try:
        cur.execute(sql,params)
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except Exception as e:
        print(e)
        conn.rollback()# 如果发生错误则回滚

        #the username has been registered,he can login in.
    if len(data) == 1:
        if(username == "admin"):
            return render_template("admin/index.html")
        else:
            return render_template('user/index.html')
     # user hasn't been registered, or passwd is wrong or he doesn't login in.
    return "You have not login in."


@app.route('/myself',methods=['POST'])
def getkey():
    session = request.form.get("session")
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    if(username is None  or passwd is None or session is None):
        status = 209
        return json.dumps({"status" : status})
    sql = "select * from Users where 3passwd2 = '%s' and session = '%s' and username = '%s' "%(passwd,session,username)
    conn.ping(reconnect=True)
    cur = conn.cursor()
    try:
        lock.acquire()
        cur.execute(sql)
        lock.release()
        data = cur.fetchall()
        conn.commit()
        cur.close()
        return json.dumps({"status" : 208, "data" : data})
    except Exception as e:
        print( e )
        conn.rollback()
        cur.close()
    return json.dumps({"status":210})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0",port=port)
