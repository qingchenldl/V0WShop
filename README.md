# V0WShop
A simple Shop based on python Flask(基于falsk的简单商店)

# 前言
一个基于`falsk+jinja2+mysql(pymysql操作)`的简单的电商系统。界面比较简陋，学习flask，做的一个简单的项目，大佬轻喷。
但是这次的项目由于从开始学习到完成只用了四天，时间实在比较短，还有很多东西没有掌握，项目还有很多不足之处，在文章的后面，我也会总结一下，以便后期完善。

# 结构搭建
## 前端
- 导航栏 base.html
	* 登录(登录以后变成退出账户)
	* 注册
	* 首页
	* 我的 (user.html)（用于记录历史以及余额等等）
- 登陆 login.html
- 注册 register.html
- 首页 index.html（由于各种因素，并由于往数据库放更多的商品。就首页这么多商品）
- 用户页面 user.html
- 商品详情 detail.html（进入商品详情页面，了解更多，并且可以在此页面完成购买）

```
采用jinja继承模板的方式，页面都继承于导航base.html
```

## 后端
- config.py
	- 数据库配置
	- SECRET_KEY
- models.py 类模型
	- User
	- Goods
- FlaskShop.py
	- /
	- /login
	- /register
	- /user/<user_id>
	- /index
	- /detail/<gid>
	- logout

## 数据库：
- user表:
	* telphone varcahr(11)主键
	* username varchar(20)
	* password varchar(32)
		 money	float
- goods表：
	* gid int 主键
	* gname varchar(30)
	* pic varcahr(10)
	* introduction varchar(100)
	* price double
	* gname varchar(20)
- history表：
	* telphone varcahr(11) 
	* gid int 
	* datetime

# 效果截图
**注册页面**
![mark](http://p1pdyrkkc.bkt.clouddn.com/blog/180831/466A2i5g1I.png?imageslim)

**登录页面：**
![mark](http://p1pdyrkkc.bkt.clouddn.com/blog/180831/A7D50AKma2.png?imageslim)

**首页**
![mark](http://p1pdyrkkc.bkt.clouddn.com/blog/180831/2L8bJJG6bg.png?imageslim)

**商品详情**
![mark](http://p1pdyrkkc.bkt.clouddn.com/blog/180831/1hjCghAFK0.png?imageslim)

**用户中心**
![mark](http://p1pdyrkkc.bkt.clouddn.com/blog/180831/Ejae9Ac8D4.png?imageslim)

# 不足之处，待完善的地方
1. **最严重的问题是内存占用率高**
	我一开始以为是我开了DEBUG模式的原因，加之浏览器处于不缓存模式，会不断请求资源，导致内存占用高。
	但是后来发现：
	不开DEBUG模式，在请求页面时，内存占用也会非常高，这是很让人头疼的，但是我也不太知道原因，麻烦知道原因的大佬，联系我`QQ:1845172981`,`邮箱：liudonglinldl@163.com`
	内存占用在请求时达到峰值，最高甚至达到80%到90%，之后会恢复到原来的水平。
2. **首页写成静态文件**
	其实应该从数据库中遍历数据，然后通过一个模板继承依次显示，但是由于懒，暂时没写。
3. **没有测试漏洞的存在与否**，如`SQL注入`，`XSS`，`CSRF`，`STTI模板注入`
	别问我为什么知道，本身就是学安全的。
4. **购买历史数据导入数据库，但是用户个人界面缺少查看购买历史的功能**
	主要是没想好功能模板放在哪，怎么写，模板没想好，第二原因：懒

------
后期完善，主要想从这几方面入手。

# 参考链接
1. [bilibili视频-python-flask零基础到项目实战](https://space.bilibili.com/349929259/#/)
2. [官方文档——中文版](http://docs.jinkan.org/docs/flask/)
3. [jinja2文档](http://docs.jinkan.org/docs/jinja2/api.html)
4. [使用pymysql笔记](http://www.zhyea.com/2015/08/20/using-pymysql.html)
