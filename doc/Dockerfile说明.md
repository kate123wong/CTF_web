Dockerfile说明：

```dockerfile
FROM ubuntu:18.04
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python3 python3-pip 
#RUN python -m pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["python3", "hello.py"]
```

从Dockerfile文件构建镜像：

```bash
docker build -t web:1.0 . #-t参数指定tag,最后的.指定上下文
docker run --name web1 -d -p 5000:5000 web:1.0
docker start 容器id #如果容器停止运行，则使用该命令使其启动
docker exec  -it 容器id /bin/bash #进入容器
```







```
 docker-compose up  #
```

