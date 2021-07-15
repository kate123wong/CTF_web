+ docker启动mysql
```bash
docker run -it --name="our_mysql"  -e MYSQL_ROOT_PASSWORD=pw-123456 -e MYSQL_DATABASE=db -e MYSQL_USER=kate -e MYSQL_PASSWORD=123456 mysql:5.6
```
