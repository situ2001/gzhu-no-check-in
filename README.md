# gzhu_no_clock_in

## 写在前面

本打卡脚本**仅供学习交流使用**，请勿过分依赖。开发者对使用或不使用本脚本造成的问题**不负任何责任**，不对脚本执行效果做出任何担保，原则上**不提供任何形式的技术支持**。

由于众所周知的**垃圾校园网**，使用**Action**自动打卡有**不小的几率会失败**，如有收到Action执行失败的通知邮件，请及时进行手动打卡。

请在下面两种方法中选择其中一种

如果觉得好用，记得**点个Star**哦

## 在本地食用

If this is your **very first time** to use the tool, please install dependencies with following command in the root dir of the cloned repo:

``` shell
pip install -r requirements.txt
```

Then, edit `stu_id.txt`, add your student id and your password in a new line. Note that id and password are separated by a blank space.

For example:

``` text
114514 19190810
111111 22222222
```

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

``` shell
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



## 配合Action食用

**首先**把该项目**Fork一份**（在网页右上角，点Fork前记得顺便**点个Star**哦~），然后去到你fork下来的仓库里。

接着，如图所示进行操作。

![Set secrets](./img/set_secrets.png)

Action会在每日7点运行，如果需要手动运行Action，可根据下图进行操作

![Run workflow](img/run_workflow.png)

如果需要关闭自动打卡功能，请根据下图所示进行手动关闭

![](./img/enable_or_disable_action.png)

如需本地运行，请参考下面的说明。

---

如果fork下来的仓库在未来出现如图所示

![](https://docs.github.com/assets/images/help/repository/fetch-upstream-drop-down.png)

则表示需要更新，点击Fetch upstream并fetch and merge即可

![](https://docs.github.com/assets/images/help/repository/fetch-and-merge-button.png)

## English Version(Outdated)

Before using this tool, you must have previously submitted health report **at least once** in `广州大学健康信息系统`!!
