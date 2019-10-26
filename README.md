* cd /Users/dongdongliao/workspace/python

* 创建Project： django-admin startproject blog

* cd blog

* 创建目录：mkdir libs（libs存放各个库文件）

* 创建home App：django-admin startapp home（App 就是 Project 中的一个功能模块）

* 安装虚拟环境：cd blog, vituralenv venv

* 启动虚拟环境: source venv/bin/activate （停止虚拟环境: deactivate ）

* 启动服务：python manage.py runserver(当前目录：****/python/blog)

* 创建目录 templates ，存放整个工程的模版文件
* 修改django中模版文件的路径配置 blog->settings.py->TEMPLATES->DIRS设置为"BASE_DIR+"/templates""

* 修改数据库配置 blog->settings.py->DATABASES

* CREATE DATABASE blog_db;
* 数据表不需要手动写sql，利用django的modes和migrate来做
	1、在models.py文件中新建class，并继承于models.Model
	2、在blog->settings.py的 INSTALLED_APPS 中加入app名，比如'home'(可以先把 INSTALLED_APPS 中默认存在的内容删掉，不然db会创建很多默认的表)
	3、命令行
		3.1 python manage.py migrate   # 创建表结构
		3.2 python manage.py makemigrations home  # 让 Django 知道我们在我们的模型有一些变更
		3.3 python manage.py migrate home   # 创建表结构



* python manage.py createsuperuser 创建一个django超级管理员(user:admin pwd:djangoadmin)

* 将需要管理的model加入到admin.py中

* 下载uikit和jquery框架， 在libs中创建css，js文件见，将下载的框架文件分别放在这两个文件夹下

* 将libs目录改名为static目录，编写home.html模版

* brew install node 安装node， 再安装插件prettify， 可以格式化css代码(node -v 查看是否安装成功,shift+command 格式化代码)
