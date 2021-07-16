from flask import Flask,render_template,request
import pymysql
import config
import base64

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

@app.route('/login',methods=['POST'])
def login():

    #获取登陆的用户名和密码
    username = request.form.get('username')
    passwd = request.form.get('passwd')

    #在数据库中查询该用户名是否注册已经密码是否正确
    cur = conn.cursor()
    sql="select * from Users where username = %s"
    params = (username)
    print(sql,params)
    try:
        cur.execute(sql,params) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
        cursor.close()
    except:
        conn.rollback()# 如果发生错误则回滚
    #如果没有注册，进入注册页面
    if len(data) == 1:
        if data[0][2] == passwd:
            print("login in ok.")
            return render_template('index.html')
        else:
            return "passwd is not right, please try again!"

    else:
        print("username",username,"has not  registered!")
        return render_template('register.html')


@app.route('/register',methods=['POST'])
def register():

    #获取注册的用户名和密码
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    
    #在数据库中查询该用户名是否已经被注册
    cur = conn.cursor()
    sql="select * from Users where username = %s"
    params = (username)
    #print(sql,params)
    try:
        cur.execute(sql,params) # 执行查询的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
        cursor.close()
    except:
        conn.rollback()# 如果发生错误则回滚
    #the username haven't been registered
    #print(len(data))
    if len(data) == 0:
        regist = 'insert into Users (username,3passwd2) values (%s, %s)'
        params_regist = (username,passwd)
        try:
            cur.execute(regist,params_regist)
            conn.commit()
            print(username ," has benn registered.")
            return render_template('login.html')
        except:
            print("something is error.")
            conn.rollback()
    else:
        print("username",username,"has been registered!")
        return "username %s has been registered! please try again" %username


@app.route('/index',methods=['POST'])
def index():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    print(username, passwd)
    
    cur = conn.cursor()
    sql="select * from Users where username = %s"
    params = (username)
    print(sql,params)
    try:
        cur.execute(sql,params) # 执行插入的sql语句
        data = cur.fetchall()
        conn.commit() # 提交到数据库执行
    except:
        conn.rollback()# 如果发生错误则回滚

        #the username has been registered,he can login in.
    if len(data) == 1:
        return render_template('index.html')
    else: # user hasn't been registered, he must register first.
        return render_template('register.html')


if __name__ == "__main__":
    app.run()
