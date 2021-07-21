FROM ubuntu:18.04
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python3 python3-pip inetutils-ping vim
#RUN python -m pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt
ADD ./fakebook /opt/fakebook/
WORKDIR /opt/fakebook
EXPOSE 5001
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["python3", "hello.py"]

