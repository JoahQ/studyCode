2020/09/12
一、git基本命令
1. git init         //初始化本地git仓库
2. git add <file>   //添加文件
3. git status       //查看状态
4. git commit       //提交
5. git push         //推送到仓库
6. git pull         //从远程仓库拉取数据
7. git clone        //从远程仓库克隆数据
8. git config --global user.name '****'        //配置
9. 8. git config --global user.email '****@**'

git commit -m '****'

二、如何忽略不想上传的文件
1. touch .gitignore   //新建.gitignore文件
2. 在.gitignore文件中输入需要忽略的文件或文件夹路径（如：log.txt;/文件夹）