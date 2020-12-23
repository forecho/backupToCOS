# backupToCOS

备份到腾讯云的 COS

## 能做什么？

- 备份指定数据库表（多个）
- 备份指定文件夹（多个）

## 如何使用？

> 只支持 Python2.6 及以上版本，推荐使用 Python3

确保已经安装了 zip，如果没安装可以执行：

```
$ sudo apt-get install zip -y
```

安装腾讯云的 COS 包

```sh
$ pip install -U cos-python-sdk-v5
```


1. 下载代码

```sh
$ git clone https://github.com/forecho/backupToCOS.git
```

2. 修改 `backup.sh` 文件配置

```sh
$ cd backupToCOS && cp backup.sh.bak backup.sh && vim backup.sh
```

3. 给 `./backup.sh` 添加执行权限，执行

```sh
$ sudo chmod +x backup.sh
```

## 添加定时任务

```sh
$ crontab -e
```

进入 cron 编辑，按 `i` 进入编辑模式，在最后输入以下内容（以下示例为每天凌晨02:00执行备份，请确认脚本路径）

```
0 2 * * * /root/backupToCOS/backup.sh
```

## 感谢

- [备份vps到七牛云存储脚本](https://github.com/ccbikai/backuptoqiniu)
- [腾讯云COS 官方 SDK](https://github.com/tencentyun/cos-python-sdk-v5)
