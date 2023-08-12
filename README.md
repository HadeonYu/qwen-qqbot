# 项目介绍
本项目把通义千问接入QQ，实现在QQ中和通义千问群聊或私聊。

项目基于go-cqhttp和通义千问api，部署本项目前请先部署好go-cqhttp，并申请和部署通义千问api。

go-cqhttp项目地址：[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，帮助文档：[docs.go-cqhttp](https://docs.go-cqhttp.org/)

通义千问api申请：[help.aliyun.com](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key?spm=a2c4g.11186623.0.0.622b7419tSwXut)

# 项目使用
1. ``main.py``中第五行的botQQ改为自己的机器人QQ号

2. ``qwn.py``中第八行改为自己的api-key
3. 运行go-cqhttp
4. 运行main.py