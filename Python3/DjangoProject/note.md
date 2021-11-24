#<center> 2021/11/24
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
