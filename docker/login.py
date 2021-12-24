import os
import re
import pickle
import msession
from ocr import ocr

def login(username: str, password: str):
    session = msession.session
    session.cookies.clear()
    res = session.get(msession.urls.cas, verify=False)
    lt = re.findall(r'name="lt" value="(.*)"', res.text)

    captcha_url = msession.urls.captcha
    captcha_path = 'captcha.jpg'
    with session.get(captcha_url) as captcha:
        with open(captcha_path, mode='wb') as captcha_jpg:
            captcha_jpg.write(captcha.content)
    captcha = ocr(captcha_path)

    login_form = {
        'username': username,
        'password': password,
        'captcha': captcha,
        'warn': 'true',
        'lt': lt[0],
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': '登录'
    }

    post_res = session.post(msession.urls.cas, data=login_form)
    
    if '账号或密码错误' in post_res.text:
        print ('账号或密码错误')
        return
    
    if '验证码不正确' in post_res.text:
        print ('验证码不正确')
        return

    os.remove('captcha.jpg')

    session.get(msession.urls.sso, verify=False)

    cookies = session.cookies

    if not os.path.exists('cookies'):
        os.mkdir('cookies')

    if not cookies:
        print ('No cookies!')
    else:
        file_name = 'cookies' + os.sep + username
        with open(file_name, mode='wb') as cookies_file:
            pickle.dump(session.cookies, cookies_file)