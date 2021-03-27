# zcgl
项目演示： http://101.133.135.36  用户名和密码是nodelete/123456  请不要修改这个密码   
此项目为比较简单的资产管理。主要包含三块，1.资产列表；2.人员列表；3.日志审计  
后端采用python3.6 + django2.2  
前端采用html + css + js  
希望你们能喜欢这个项目，有bug可以联系我(yangbhust@163.com)  
项目的经过可以看本人博客https://www.cnblogs.com/ddzj01/p/11316837.html  
这个项目放到网上之后，有不少人发邮件给我，说不知道如何启动项目，了解下来，基本上都是刚接触django的，想通过这个简单的项目来学习如何使用django。为了不误人子弟，特意将该项目重写了一遍，尽量做到代码和命名规范。并在readme.md中介绍如何启动项目。  

# 如何启动项目
1. 创建数据库，create database zcgl;  
2. 创建数据库用户，grant all on zcgl.* to scott@'%' identified by 'tiger';  
3. 将settings.py中DATABASES进行相关修改  
4. 安装相关包，pip install -r requirements.txt，如果是linux环境还需要先修改requirements.txt    
5. 迁移数据库，python manage.py migrate  
6. 创建超级用户，python manage.py createsuperuser  
6. 启动项目，python manage.py runserver 0.0.0.0:8000  

# 下面是项目的部分截图
首页
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/index.png)

登录
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/login.png)

资产列表
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/serlist.png)

资产类型
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/sertype.png)

添加资产
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/seradd.png)

资产详情
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/serdetail.png)

人员管理
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/persondetail.png)

日志记录
![Image text](https://github.com/YangBaohust/myimages/blob/master/zcgl/log.png)
