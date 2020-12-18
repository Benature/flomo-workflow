<a href="https://flomoapp.com/"><img src="./media/logo-192x192.png" height="100" align="right"></a>

# flomo workflow

一个非官方的 API python 玩具盒

- 【播客】[小宇宙url 👉 flomo memo](./xyz2flomo.py)
  - Alfred + flomo ([demo 视频](https://m.okjike.com/originalPosts/5fc1e8f0c5e485001882a2be?s=ewoidSI6ICI1ZWUxZDQ1OGY5MmZiYzAwMTc3NWMwZTgiCn0=))
- 发送新的 flomo memo
- 按模板创建 memo (inspired by [即刻@阿粒](https://m.okjike.com/reposts/5fc72ccb88f60f00189b1aa3?s=ewoidSI6ICI1ZWUxZDQ1OGY5MmZiYzAwMTc3NWMwZTgiCn0=))
- [批量改 tag](replace_tag.py)

> *prefer python3.7+*  
> 欢迎 Star 🌟、Fork 🍴、Issue 💬、PR. 一起让 flomo 用的更加得心应手

## Usage 使用

安装 [flomo 包](https://github.com/Benature/flomo)

```shell
pip install -U flomo
```

将 [`config_sample.py`](./config_sample.py) 更名为 `config.py`

### Cookies

如图配置 cookies

<p align="center">
  <a href="#" target="_blank"><img src="https://i.loli.net/2020/12/06/T13IJEKMyPX89us.png"  width="80%"></a>
</p>

[...待补充](https://www.notion.so/benature/flomo-0061a1c4d4b643c58a9855aa8a28e0fb)

### Notify 通知

详细说明见 [About Notification 关于通知](#about-notification-关于通知)

配置参照 [terminal-notifier](https://github.com/julienXX/terminal-notifier#options)

### Template 模板

- `path`: 模板路径
- `time_format`: 日报日期格式

默认模板为[日报](./templates/daily.html)，可自行修改格式

## Workflow

### Alfred (macOS)

[workflow 下载](https://github.com/Benature/flomo/releases/download/v0.0.2-alpha/flomo.alfredworkflow)

代码没有放在 workflow 里面，需要根据各位电脑稍做适配:  
在 `Run Script` 中

- `python` 命令需要修改为电脑中 `python3` 的路径 (eg. `/Users/xxx/miniconda3/bin/python.app`)
- `.py` 文件的**绝对路径**修改为仓库所在路径 (eg. `/Users/xxx/Documents/Github/FUN/flomo/flomo.py`)


### Wox (Windows)

*TBD...*

## About Notification 关于通知

（macOS）有以下两种通知方法来实现：

- apple script
- **[terminal-notifier](https://github.com/julienXX/terminal-notifier)** (recommended)

推荐后者，前者简单粗暴，后者好处在于

- 设置了 logo
- 可自定系统提示音
- 支持点击通知后跳转到 flomo app
  - 跳转到 Chrome app
  - 跳转到 [flomoapp.com](https://flomoapp.com/) 网页

不过需要另外安装

```shell
brew install terminal-notifier
```

---

# Relative Project 相关项目

- pip: [Benature/flomo](https://github.com/Benature/flomo)
- npm: [geekdada/flomo api helper](https://github.com/geekdada/flomo-api-helper)

# Demo

<!-- <br/> -->
<p align="center">模板生成</p>
<p align="center">
  <a href="#Demo" target="_blank"><img src="https://i.loli.net/2020/12/06/45me2k8qAMjhGrT.gif" width="80%"></a>
</p>