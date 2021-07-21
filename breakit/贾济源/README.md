ip：10.195.25.17

使用namp扫描：

![image-20210721095431062](README.assets/image-20210721095431062.png)

访问:http:10.195.25.17:3389

发现连接被重置

![image-20210721095634773](README.assets/image-20210721095634773.png)

界面中有一`猜猜我是谁`图片，下载发现名称为`flag.png`  
用`binwalk`查看发现有一压缩包，打开压缩包有`tips.txt`  
打开发现为一段base64编码，解码内容  
![base64](README.assets/base64.png)