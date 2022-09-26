import os
from login_new import login_new
from clock_in import clock_in
import requests
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import telegram


def main():
    students = {}

    with open('stu_id.txt', mode='r') as f:
        for line in f:
            stu = line.split(' ')
            stu = [x.strip() for x in stu]
            students[stu[0]] = stu[1]

    for id in students:
        print('学生已加载: {}'.format(id))

    print('开始打卡...')
    print()

    MAX_RETRY_COUNT_LOGIN = 4
    MAX_RETRY_COUNT_CLOCKIN = 10

    summary = {}

    for id in students:
        print("当前学号:", id)
        login_status = False
        clock_in_status = False
        try:
            print("登录中...")
            count_login = 1
            login_status = login_new(id, students[id])
            while not login_status and count_login <= MAX_RETRY_COUNT_LOGIN:
                print("登录失败 重试中 次数:", count_login)
                login_status = login_new(id, students[id])
                count_login += 1
            print("打卡中...")
            count_clockin = 1
            clock_in_status = clock_in(id)
            while not clock_in_status and count_clockin <= MAX_RETRY_COUNT_CLOCKIN:
                print("打卡失败 重试中 次数:", count_clockin)
                login_status = login_new(id, students[id])
                while not login_status and count_login <= MAX_RETRY_COUNT_LOGIN:
                    print("登录失败 重试中 次数:", count_login)
                    login_status = login_new(id, students[id])
                    count_login += 1
                clock_in_status = clock_in(id)
                count_clockin += 1
        except:
            print("失败了，当前学号", id, "\n")
        summary[id] = (login_status, clock_in_status)

    print()
    result_str = ''
    all_status = True
    student_num = 0
    clocked = 0
    for stu in summary:
        (l, c) = summary[stu]
        if c : 
            clocked += 1
        all_status &= l and c
        result_str += ('学号 {} 登录 {} 打卡 {}\n'.format(stu, l, c))
        student_num += 1
    if all_status:
        status_string = "打卡成功({}/{})".format(clocked, student_num)
    else:
        status_string = "打卡失败({}个成功，{}个失败)".format(clocked, student_num - clocked)
    print(result_str)

    # if SCT_KEY is set
    if os.getenv('SCT_KEY'):
        key = os.getenv('SCT_KEY')
        now = datetime.now()
        y, m, d, h, min, sec, wd, yd, i = now.timetuple()
        payload = {
            'title': '{}/{}/{} 健康打卡:{}'.format(y, m, d, status_string),
            'desp': result_str
        }
        requests.get(
            'https://sctapi.ftqq.com/{}.send'.format(key), params=payload)

    # if PPTKEY is set
    if os.getenv('PPTKEY'):
        token = os.getenv('PPTKEY')
        payload = {
            'token': token,
            'title': '健康打卡:{}'.format(status_string) ,
            'content': result_str,
            'template': 'html'
        }
        requests.get('http://www.pushplus.plus/send', params=payload)

    # if you have termux-api
    if os.name == 'posix':
        os.system(
            '[ -x $PREFIX/libexec/termux-api ]&&termux-notification -t "{}"'.format(result_str))
#    elseif os.name == 'nt' : 这里打算做win10toast

    # Telegram push by Yuzi0201
    if os.getenv('TELETOKEN') and os.getenv('TELECHATID'):
        token = os.getenv('TELETOKEN')
        chat_id = os.getenv('TELECHATID')
        # 设置代理，如服务器在境外则不需要
        # proxy_http=os.getenv('TG_HTTP_PROXY')
        #proxy = telegram.utils.request.Request(proxy_url=proxy_http)
        #bot = telegram.Bot(token, request=proxy)
        bot = telegram.Bot(token)
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
        if "," in chat_id:  # 多用户支持
            chat_id = chat_id.split(",")
            for id in chat_id:
                bot.send_message(id, text=str(bj_dt.month) +
                                 "月"+str(bj_dt.day)+"日的打卡结果：\n"+result_str)
        else:
            bot.send_message(chat_id, text=str(bj_dt.month) +
                             "月"+str(bj_dt.day)+"日的打卡结果：\n"+result_str)


main()
