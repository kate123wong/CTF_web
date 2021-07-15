+ [flask官方文档](https://flask.palletsprojects.com/en/2.0.x/installation/)

+ 测试环境：python:3.9.2
+ 安装过程：
```bash
mkdir system
cd system
sudo apt install python3-venv 
python3 -m venv venv
 . venv/bin/activate #激活环境
 pip install Flask # 安装Flask
```

+ 编写flask文件：hello.py
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
```
注意：flask文件名称不能为falsk.py,为app.py/wsgi.py时不需要设置环境变量（具体细节参考[官方文档](https://flask.palletsprojects.com/en/2.0.x/cli/) ）

+ 启动：
在linux系统运行bash脚本

```bash
 export FLASK_APP=hello
flask run
 * Running on http://127.0.0.1:5000/
```

+使用` flask run --host=0.0.0.0`可以使其他机器可以访问我们的网页。
