# gzhu_no_clock_in

## 如何食用

首先把该项目Fork一份（在网页右上角，记得顺便点个Star哦~），然后去到你fork下来的仓库里。

接着，如图所示进行操作。

![Set secrets](./img/set_secrets.png)

Action会在每日7点运行，如果需要手动运行Action，可根据下图进行操作

![Run workflow](img/run_workflow.png)

如需本地运行，请参考下面的说明。

未来计划：稳定后将支持telegram或企业微信推送打卡结果。

---

## English Version(Outdated)

如下为本地使用指南，并且略有过期。

Note: **Early version**

AND you must save a **template** in `广州大学健康信息系统`!!

## How to use

If this is your **very first time** to use the tool, please install dependencies with following command:

``` shell
pip install -r requirements.txt
```

If you are a Windows user, please install `tesseract` from this [link](https://digi.bib.uni-mannheim.de/tesseract/) and add to PATH.

Or if you use linux, just run your software package manager to install `tesseract`. For instance, installing this package can be done by running this command.

```shell
apt install tesseract
```

Then, edit `stu_id.txt`, add your student id and your password in a new line. Note that id and password are separated by a blank space.

For example:

``` text
114514 19190810
111111 22222222
```

Run.

``` shell
python run.py
```

If `打卡成功` appears, you are free of the nettlesome clock in.

## ~~I am from the future~~

This function is **Invalidated from 2021/06/10**

~~(puns)So you can return to the past to check in. If you want to check in from 3-10(inclusive) to 3-16(inclusive), type and run this command.~~

``` shell
# python run.py -d 7
```

## TODO

- [x] ~~check in ahead of schedule~~
- [ ] try to login or clock in if failed.
- [ ] use another approach to recognize instead of tesseract OCR
