#### 1、Git bash设置中文编码为
```shell

git config --global core.quotepath false          # 显示 status 编码
git config --global gui.encoding utf-8            # 图形界面编码
git config --global i18n.commit.encoding utf-8    # 提交信息编码
git config --global i18n.logoutputencoding utf-8  # 输出 log 编码
export LESSCHARSET=utf-8                          # less 分页编码

```

