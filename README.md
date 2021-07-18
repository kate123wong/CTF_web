# CTF_web

## 小组成员

王冬霞 张欣怡 马君瑞

### 说明
+ 过程源代码：src文件夹
+ 文档及说明：doc文件夹

### 时间安排

| 时间                      | 具体安排                                                     | 是否按时完成 |
| ------------------------- | ------------------------------------------------------------ | ------------ |
| 2021.7.15上午             | 确定大致的项目需求、漏洞利用链、创建github私有仓库、指定进度；学习flask和mysql相关内容 | 是           |
| 2021.7.15下午-2021.7.17晚 | 完成前后端、漏洞利用链的开发工作                             |              |
| 2021.7.18-2021.7.19       | 完成exp、check脚本编写；完成docker部署、初步完成文档         |              |
| 2021.7.20-                | 完成文档完善、完成展示PPT的制作                              |              |

### 前后端开发注意事项：  

**数据库中name等字段存在长度限制，flask相关代码部分需要进行实现长度限制的完善，以免接收过长数据数据库端报错**

+ 用户密码取md5hash、admin账号是base64编码值

+ key放在admin的备注里

+ 前端个人主页

+ 密码用户名特殊字符过滤

+ 评论可以显示、传后端

+ 数据库payload=`1'or'1'=='1`,url是：`http://hostip/index`.

  `http://hpstip/index?id=1'or'1'=='1`可以返回User数据库，可以得到admin的密码和key字段的值。

### 二维码相关工作均已完成 
* admin二维码 `admin.png`  
[二维码](https://github.com/kate123wong/CTF_web/blob/development/doc/%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3/image/admin.png)  
* 普通二维码 `origin1.png`  
[二维码](https://github.com/kate123wong/CTF_web/blob/development/doc/%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3/image/origin1.png)
=======
**数据库中name等字段存在长度限制，flask相关代码部分需要进行实现长度限制的完善，以免接收过长数据数据库端报错**

