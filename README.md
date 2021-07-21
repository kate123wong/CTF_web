# CTF_web

## 小组成员

王冬霞 张欣怡 马君瑞

## Start

+ 从Dockerfile构建：

  >进入source目录，运行`docker-compose up`,访问：`localhost:5000`

+ 直接从镜像启动服务（推荐：不依赖本除同级目录下的`docker-compose.yml`文件外的任何本仓库文件）：

  >在本文件同级目录下，运行`docker-compose up`,访问：`localhost:5000`

  **注意：如果本地5000端口被占用,可能导致服务启动失败**

### 说明
+ docker构建代码：source文件夹
+ 文档及说明：doc文件夹
+ exp：exp文件夹
  - [ ] exp.py是可完成：对于`指定的ip、姓名、密码`可注册、登陆、获取session后进行sql注入，得到admin的密码并（通过暴力破解md5得到）登陆admin账号。获取带有flag值的二维码文件并获得flag
+ check：check文件夹
  + 可以指定姓名、密码

### 时间安排

| 时间                      | 具体安排                                                     | 是否按时完成 |
| ------------------------- | ------------------------------------------------------------ | ------------ |
| 2021.7.15上午             | 确定大致的项目需求、漏洞利用链、创建github私有仓库、指定进度；学习flask和mysql相关内容 | 是           |
| 2021.7.15下午-2021.7.17晚 | 完成前后端、漏洞利用链的开发工作                             | 是           |
| 2021.7.18-2021.7.19       | 完成exp、check脚本编写；完成docker部署、初步完成文档         | 是           |
| 2021.7.20-～              | 完成文档完善、完成展示PPT的制作                              |              |

### 前后端开发注意事项：  

- [x] 用户密码取md5hash
- [x] key放在admin的备注里
- [x] 前端个人主页
- [x] 数据库payload=`1'or'1'=='1`,注入点是个人主页的username字段.:数据库中name等字段存在长度限制，flask相关代码部分需要进行实现长度限制的完善，以免接收过长数据数据库端报错

### 二维码相关工作均已完成 
* admin二维码 `admin.png`  
  [二维码](https://github.com/kate123wong/CTF_web/blob/development/doc/%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3/image/admin.png)  

* 普通二维码 `origin1.png`  
  
  [二维码](https://github.com/kate123wong/CTF_web/blob/development/doc/%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3/image/origin1.png)

