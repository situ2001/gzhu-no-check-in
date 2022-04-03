# gzhu_no_clock_in

## 写在前面

本脚本**仅供学习交流使用**，请勿过分依赖。

开发者对使用或不使用本脚本造成的问题**不负任何责任**，不对脚本执行效果做出任何担保，原则上**不提供任何形式的技术支持**。

觉得好用，可以**点个 Star**支持

Before using this tool, you must have previously submitted health report **at least once** in `健康信息系统`!!

## Use locally

If this is your **very first time** to use the tool, please install dependencies with following command in the root dir of the cloned repo:

```shell
pip install -r requirements.txt
```

Then, edit `stu_id.txt`, add your student id and your password in a new line. Note that id and password are separated by a blank space.

For example:

```text
114514 19190810
111111 22222222
```

ServerChan, pushpush and telegram notification push are supported.

### In addition, you can set env variable `SCT_KEY` or `PPTKEY` with your SendKey of ServerChan or PushPlus push service to receive result on your WeChat

For example, setting env variable on Ubuntu/Debian

```shell
export SCT_KEY=<YOUR_SEND_KEY>
#if you have `SCT_KEY`
```

Or

```shell
export PPTKEY=<YOUR_PUSHPLUS_TOKEN>
#if you have `PPTKEY`
```

And run.

```shell
python run.py
```

#### Or combining them together.

```shell
export SCT_KEY=<YOUR_SEND_KEY> ;python run.py
```

Or

```shell
export PPTKEY=<YOUR_PUSHPLUS_TOKEN>;python run.py
```

### You can also set env variables `TELETOKEN` and `TELECHATID` with your telegram bot token and your telegram user id(for multi user,you can spilt your id with ",")

For example, setting env variable on Ubuntu/Debian

```shell
export TELETOKEN=YOUR TOKEN
export TELECHATID=CHATID1,CHATID2,CHATID3...
python run.py
```

### You can also schedule a task with `cron`. For example, if you want to execute the task at 7:10 everyday, you can appending this line to cron file.

Just only execute :

```shell
10 7 * * * cd /path/to/gzhu_no_clock_in && python run.py
```

Or with `SCT_KEY` :

```shell
10 7 * * * export SCT_KEY=<YOUR_SEND_KEY> && cd /path/to/gzhu_no_clock_in && python run.py
```

Or with `PPTKET` :

```shell
10 7 * * * export PPTKEY=<YOUR_PUSHPLUS_TOKEN> && cd /path/to/gzhu_no_clock_in && python run.py
```

## 配合 Action 食用

This feature was removed due to high failure rate. And the author of this repo will not maintain it.

If you want to help fix it, please raise a PR :)
