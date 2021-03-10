# gzhu_no_clock_in

Note: **Early version**

AND you must save a **template** in `广州大学健康信息系统`!!

## How to use

If this is your **very first time** to use the tool, please install dependencies with following command:

``` shell
pip install -r requirements.txt
```

And install `tesseract` from this [link](https://digi.bib.uni-mannheim.de/tesseract/) and add to PATH.

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

## I am from the future

(puns)So you can return to the past to check in. If you want to check in from 3-10(inclusive) to 3-16(inclusive), type and run this command.

``` shell
python run.py -d 7
```

## TODO

- [x] check in ahead of schedule
- [ ] try to login or clock in if failed.
- [ ] use another approach to recognize instead of tesseract OCR
