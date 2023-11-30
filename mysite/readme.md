django-admin startproject mysite

创建django项目

python manage.py runserver

python manage.py runserver 8080

python manage.py runserver 127.0.0.1

运行django项目可选参数改变ip和port端口
python manage.py startapp polls

创建app polls
python manage.py migrate

数据库注入
从installed_app中
python manage.py makemigrations polls

注入polls的module中的类建立
python manage.py sqlmigrate polls 0001显示将要注入的数据的sql语句
python manage.py migrate

注入sql语句
处理数据库三步走

Cpython manage.py migrate   # 创建表结构
 
python manage.py makemigrations polls  # 让 Django 知道我们在我们的模型有一些变更

python manage.py migrate polls   # 创建表结构

第一步：

    删除该app名字下的migrations下的__init__.py等文件。

第二步：

    进入数据库，找到django_migrations的表，删除该app名字的所有记录。

第三步：执行下面这两条命令：（在项目目录下）

python manage.py makemigrations

python manage.py migrate




python manage.py shell
打开python的shell
python manage.py createsuperuser
创建超级用户
user:zzh
password:12345678ab
![截屏2023-11-27 11.50.57.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F4y%2Fprx069v50psfkkq5q_23r9jw0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_n1L4Db%2F%E6%88%AA%E5%B1%8F2023-11-27%2011.50.57.png)
此处可看数据库变化
