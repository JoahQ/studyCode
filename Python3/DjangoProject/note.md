# <center>  2021/11/24  </center>

#### 1.创建一个Django项目“mysiteproject”
方法1:  
```shell
$: django-admin startproject mysiteproject
```
方法2:  
```shell
$: django-admin startproject mysiteproject .
```
#### 2.启动服务
```shell 
$: python manage.py runserver
```
#### 3.创建应用“myblog”
```shell
$: python manage.py startapp myblog
```
#### 4.django-admin命令  
```shell
$: django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTAL
LED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or ca
ll settings.configure() before accessing settings.).
```
#### 5.python manage.py命令
　　在创建一个Django项目后，manage.py在项目的根目录中被自动生成，它是对django-admin
.py的简单封装，同样能够实现命令行操作：
```shell
python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

```
# <center>  2021/11/25  </center>  
#### 1.根据模型建立数据库表命令
```shell
$: python manage.py makemigrations

Migrations for 'myblog':
  myblog\migrations\0001_initial.py
    - Create model BlogArticles
```
上面创建了一个能够建立数据库表的文件，下面就在此基础上，真正创建数据库了
（注意操作指令时所在的目录位置）。
```shell
$: python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myblog, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying myblog.0001_initial... OK
  Applying sessions.0001_initial... OK
```

#### 2.创建超级管理员
```shell
$: python manage.py createsuperuser

Username (leave blank to use 'dell1'): zhou
Email address: admin@admin
Error: Enter a valid email address.
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

#### 3.交互模式中练习对数据库的增、删、查、改的操作  
使用python manage.py shell的方式进入交互模式，用这种方式已经将
Django环境引入到了当前交互模式中。
```shell
$: python manage.py shell

>>> from django.contrib.auth.models import User
>>> from myblog.models import BlogArticles
>>> user = User.objects.get(username="zhou")
```
面这行语句的含义是获取User数据模型的字段username是zhou的那个对象,
或者数是数据库表auth_user中字段值是zhou的那条记录（也是对象），
所以user就是一个包含多个字段值的对象实例。
```shell
>>> user.username
'zhou'
>>> user.id
1
>>> user.password
'pbkdf2_sha256$260000$YjqFwTZ0W1HhnfHCqTBr3L$6xExAnBOfMkNFgeUgGP5OlZb+o2UNYSC0tZlEI81AX0='
>>> type(user)
<class 'django.contrib.auth.models.User'>
```
也可以将数据库中所有记录读取出来。
```shell
>>> users = User.objects.all()
>>> users
<QuerySet [<User: zhou>, <User: qq>]>
>>> blogs = BlogArticles.objects.all()
>>> blogs
<QuerySet [<BlogArticles: 中国现代诗歌>, <BlogArticles: 望庐山瀑布>, <BlogArticles: 将进酒>, <BlogArticles: 静夜思>, <B
logArticles: Ubuntu环境下python环境的搭建以及pycharm的安装>]>
>>> for blog in blogs:
...     print(blog.title)
...
中国现代诗歌
望庐山瀑布
将进酒
静夜思
Ubuntu环境下python环境的搭建以及pycharm的安装
>>>
```