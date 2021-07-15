## ubuntu18.04下docker环境搭建

+ [官方文档](https://docs.docker.com/engine/install/ubuntu/)

## 过程

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

## 测试

```bash
sudo docker run hello-world
```

## 启动mysql

```bash
docker run -itd --name ctf-web-mysql -e MYSQL_ROOT_PASSWORD=6iuVhYwmxC -e MYSQL_DATABASE=socialcontact -e MYSQL_USER=socialcontact -e MYSQL_PASSWORD=socialcontact123 mysql:5.7
```

+ [参考代码](https://github.com/alexferl/flask-mysqldb)
