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

3. git branch mybranch1  //创建分支
4. git checkout mybranch1 //切换到mybranch1分支
5. git merge mybranch1 //在主分支master下执行此命令合并mybranch1分支

冲突解决方案有三种：
1. 无视，直接commit自己的代码。
git commit -m "your msg"
2. stash

stash翻译为“隐藏”，如下操作：

git stash
git pull
git stash pop
然后diff一下文件，看看自动合并的情况，并作出需要的修改。

git stash: 备份当前的工作区的内容，从最近的一次提交中读取相关内容，让工作区保证和上次提交的内容一致。同时，将当前的工作区内容保存到Git栈中。
git stash pop: 从Git栈中读取最近一次保存的内容，恢复工作区的相关内容。由于可能存在多个Stash的内容，所以用栈来管理，pop会从最近的一个stash中读取内容并恢复。
git stash list: 显示Git栈内的所有备份，可以利用这个列表来决定从那个地方恢复。
git stash clear: 清空Git栈。

3. 硬覆盖：放弃本地修改，直接用git上的代码覆盖本地代码：

git reset --hard
git pull
