import pymysql
import config

conn=pymysql.connect(host = config.host # 连接名称，默认127.0.0.1
,user = 'root' # 用户名
,passwd='6iuVhYwmxC' # 密码
,port= 33069 # 端口，默认为3306
,db='socialcontact' # 数据库名称
,charset='utf8' # 字符编码
)

cur = conn.cursor()
sql="select * from `user`"
try:
    cur.execute(sql) # 执行插入的sql语句
    data = cur.fetchall()

    for i in data[:]:
        print (i)

    conn.commit() # 提交到数据库执行
except:
    conn.rollback()# 如果发生错误则回滚

conn.close() # 关闭数据库连接

