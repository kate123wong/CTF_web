from flask import Flask,render_template, request
from hashlib import md5    
import requests
import pymysql
import config
import base64
import json
import time
import random

conn=pymysql.connect(host = config.host # 连接名称，默认127.0.0.1
,user = 'root' # 用户名
,passwd='6iuVhYwmxC' # 密码
,port= 33069 # 端口，默认为3306
,db='socialcontact' # 数据库名称
,charset='utf8' # 字符编码
)


app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('login.html')


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
    cur = conn.cursor()
    sql="select * from Users where username = %s"
    params = (username)
    try:
        cur.execute(sql,params) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except:
        conn.rollback()# 如果发生错误则回滚
    if len(data) == 1:
        #只要用户已经注册并且密码正确，就重新生成session值，不管现在是否是登陆状态。
        if data[0][2] == passwd:
            session = md5((str(time.time()) + str(random.random()) ).encode('utf8')).hexdigest()
            sql_set_session = "update Users set session= %s where username= %s and 3passwd2= %s"
            params_set_session = (session,username,passwd)
            try:
                cur.execute(sql_set_session,params_set_session)
                conn.commit()
                status = 206 # 成功登陆
                return json.dumps({ 'status': status, 'session' : session})
            except Exception as e:
                print("failed login in")
                conn.rollback()
                status = 207 #登陆失败
        else:
            status = 205
    else:
        # print("username",username,"has not  registered!")
        # return render_template('register.html')
        #html = render_template('register.html')
        status = 201
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
    cur = conn.cursor()
    sql="select * from Users where username = %s"
    #sql="select * from Users where username = '" + username + "';"
    params = (username)
    #print(sql)
    data = tuple()
    try:
        cur.execute(sql,params) # 执行查询的sql语句
        #cur.execute(sql) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
        cur.close()
    except:
        conn.rollback()# 如果发生错误则回滚
    #the username haven't been registered
    print(data)
    if len(data) == 0:
        regist = 'insert into Users (username,3passwd2) values (%s, %s)'
        print(regist)
        params_regist = (username,passwd)
        try:
            cur.execute(regist,params_regist)
            conn.commit()
            status = 202 #注册成功
            print("success!")
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
    print(username,passwd,session)
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
        print(e)
        conn.rollback()# 如果发生错误则回滚

        #the username has been registered,he can login in.
    if len(data) == 1:
        status = 208
        html = render_template('index.html')
        return json.dumps({"status" : status, "html" : html})
     # user hasn't been registered, or passwd is wrong or he doesn't login in.
    return json.dumps({"status" : 207})

@app.route('/user/index',methods=['GET'])
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
        return render_template('user/index.html')
     # user hasn't been registered, or passwd is wrong or he doesn't login in.
    return "You have not login in."


@app.route('/key',methods=['GET'])
def getkey():

    uid = request.args.get("id")
        
    print(uid)

    #username = request.args.get('username')
    #passwd = request.args.get('passwd')
    #if(!username || !passwd):
    #    return "username or password doesn't"
    #sql = "select * from Users where username = %s and passwd = %s"
    #sql = "select * from Users where username = '%s' and 3passwd2 = '%s' "%(username,passwd)
    sql = "select * from Users where uid='%s' "%(uid)
    print(sql)
    cur = conn.cursor()
    try:
        #cur.execute(sql,params)
        cur.execute(sql)
        data = cur.fetchall()
        conn.commit()
        print("data is:",data)
        return "message:"+json.dumps(data)
    except Exception as e:
        print( e )
        conn.rollback()
    return "user doesn't existed or the password is wrong!"


if __name__ == "__main__":
   app.run()
