# Git使用筆記

* 查看git檔案狀態
```
git status
```

* 查看git commit log 狀態
```
git log

//跳出方式:
按ESC ， 再輸入q
```

* 查看git commit log 狀態 - 炫泡指令
```
git log --oneline
```

* 追蹤檔案
```
git add "檔名"
```

* 追蹤所有更動過的檔案
```
git add .
```

* 紀錄
```
git commit -m "輸入這次修改的文字描述訊息"
```

* 把紀錄推到遠端線上
```
git push -u origin master 

//若有設定過遠端指定分支

git push
```

* 查看git分支
```
git branch -a
```
* 查看git遠端來源庫
```
git remote
```
* 新增分支
```
git branch 分支名稱
```
* 切換git分支
```
git checkout "branch名稱"
```
* 新增分支並且同時切換到該分支
```
git checkout -b "分支名稱"
```
---
### 推薦文章
[推薦協作文件平台](https://hackmd.io/)

[[文件] 前端打包迷你化](https://hackmd.io/VWibUPGzSWeJyGOqitb5CA)
