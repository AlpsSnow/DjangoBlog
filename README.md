# DjangoBlog
使用Django搭建一个博客系统


### 安装
1.```pip install -r requirement.txt ```

2.`setting.py`配置自己的数据库 

3.```python manage.py makemigrations ``` 

4.```python manage.py migrate```  

5.```python manage.py runserver```  

### django开发blog
1. [起步](./readme/起步.md)  
2. [应用与路由](./readme/应用与路由.md)  
3. [模板](./readme/模板.md)  
4. [后台管理](./readme/后台管理.md)  
5. [数据库和模型迁移](./readme/数据库和模型迁移.md)  
6. [用户注册](./readme/用户注册.md)  
7. [用户登录与注销](./readme/用户登录与注销.md)  
8. [用户profile和上传图片](./readme/用户profile和上传图片.md)  
9. 更新用户信息
10. 博文的增删改查
11. 博文列表的分页展示
12. 发送邮件重置用户密码
13. 部署到linux服务器
14. [使用vscode调试django](./使用vscode调试django.md) 

### TODO
1. 重置密码技能，依然存在问题
> ConnectionRefusedError at /password_reset/  
[WinError 10061] 由于目标计算机积极拒绝，无法连接。

即使[获取qq邮箱的授权码后](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)，依然存在上面的问题，还需继续调查。

网络检索发现同样问题：https://blog.csdn.net/Dick633/article/details/83714266
