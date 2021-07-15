## MYSQL搭建

+ [官方文档](https://docs.docker.com/engine/install/ubuntu/)

## docker搭建过程

```bash
udo apt-get update

 sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

#x86_32/amd64(其他架构的系统详见官方文档)
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
  sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

### docker测试

```bash
sudo docker run hello-world
```

## mysql

### 启动mysql

```bash
docker run -itd --name ctf-web-mysql -p 33069:3306 -e MYSQL_ROOT_PASSWORD=6iuVhYwmxC -e MYSQL_DATABASE=socialcontact -e MYSQL_USER=socialcontact -e MYSQL_PASSWORD=socialcontact123 mysql:5.7
# docker内部的3306端口(对应mysql)映射到主机的33069端口。
```

+ [参考代码](https://github.com/alexferl/flask-mysqldb)

### 命令行进入mysql操作

```
docker exec  -it 容器id /bin/bash
mysql -h localhost -u root -p6iuVhYwmxC
```

### mysql语法

```mysql
SHOW DATABASES; #显示所有的数据库
CREATE DATABASE test_db;#创建数据库
SHOW DATABASES LIKE '%socialcontact%'; #显示文件名含有socialcontact的数据库
USE socialcontact;#使用socialcontact数据库
SHOW TABLES; #列出所有的表
CREATE TABLE user(name VARCHAR(25)); #创建表
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN ); # 插入语句
INSERT INTO user (name) VALUES ('kate');
```

### Python连接mysql

```python
import pymysql

conn=pymysql.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1
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
```

