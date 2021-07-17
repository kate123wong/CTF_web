# flask测试样例

## 结构说明

**static**存放网页所需的css等

**templates**存放.py文件和主要html

**login.html**登陆界面

![](img/login效果图.png)

**register.html**注册界面

![](img/register效果图.png)

**index.html**首页界面

![](img/首页效果图.png)

**test.py**调用html的测试样例，执行时cd到test目录下然后

`export FLASK_APP=test`

`flask run`

**templates/admin**存放admin用户的个人主页index.html

**admin/index.html**个人主页界面，破解后可见

![](img/admin效果图.png)

**user/index.html**个人主页界面，用户登录后可见

![](img/user效果图.png)



## 需求分析

- index.html的href里需要添加个人主页的链接
