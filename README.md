# zhuye_kim
仿zhuye.kim的简单导航程序



#### 使用说明 ####


- 安装Python3和必备组件、库

Centos7系统安装Python3可以参考文章：http://blog.51cto.com/wenguonideshou/2083301



配置好Python3.6和pip3 安装EPEL和IUS软件源
```
yum install epel-release -y
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
```
安装Python3.6
```
yum install python36u -y
```
创建python3连接符
```
ln -s /bin/python3.6 /bin/python3
```
安装pip3
```
yum install python36u-pip -y
```
创建pip3链接符
```
ln -s /bin/pip3.6 /bin/pip3
```
```
bash
yum install git screen -y
pip3 install django pymysql pillow
```

- 使用宝塔面板或其他方式安装mysql（mariadb也可以），新建数据库名为zhuye

- 修改zhuye_kim/settings.py中的DATABASES对应的数据库信息（只需要修改数据库密码）

- 下载源码、建表

```bash
git clone https://github.com/wenguonideshou/zhuye_kim
cd zhuye_kim
python3 manage.py makemigrations --merge
python3 manage.py makemigrations
python3 manage.py migrate
```
（如果是python2  3共存 前面替换成 pyhton3.6  详细版本号）

- 导入zhuye.sql

- 运行网站
```bash
screen -S zhuye
python3 manage.py runserver 127.0.0.1:8001
 ```
 	 
- Nginx反向代理

![反向代理.png](https://i.loli.net/2018/07/17/5b4df8524ab67.png)	

后台地址为http://ip/admin，如果已经绑定域名反向代理则为http://域名/admin，管理员用户名admin密码12345678@


后台的“大分类”指的是常用/男生/女生 这一行，“小分类”指的是热门/资讯/影音/邮箱的这一列

更新记录：

2018-07-26 增加更换背景图功能，发布1.1版

2018-07-19 修复百度搜索关键字联想功能，发布1.0版

2018-07-18 补全导航中所有站点、图标

2018-07-17 去除多引擎，修改为默认单引擎

2018-07-16 发布beta版

**获取更多帮助请[加群](http://shang.qq.com/wpa/qunwpa?idkey=d119da6023cc49729a61139ca4b8bb0ee770d8d9a89383939c4a45159f82bc6d)**

