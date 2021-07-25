from requests import adapters


def login_new(username: str, password: str):
    import execjs

    with open('./js/des.js') as f:
        fn_js = f.read()

    ctx = execjs.compile(fn_js)
    
    from msession import session, urls
    import re

    session.cookies.clear()

    res = session.get(urls.cas_new, verify=False)
    lt = re.findall(r'name="lt" value="(.*)"', res.text)

    enc_target = username + password + lt[0]

    result_rsa = ctx.call('strEnc', enc_target, '1', '2', '3')

    form = {
        'rsa': result_rsa,
        'ul': str(len(username)),
        'pl': str(len(password)),
        'lt': lt[0],
        'execution': 'e1s1',
        '_eventId': 'submit',
    }

    from requests.adapters import HTTPAdapter
    adapter = HTTPAdapter(max_retries=10)
    session.mount(urls.cas_new, adapter=adapter)
    res = session.post(urls.cas_new, data=form, timeout=30)

    cookies = session.cookies
    
    import os
    import pickle

    if not os.path.exists('cookies'):
        os.mkdir('cookies')

    if not cookies:
        print ('No cookies!')
    else:
        file_name = 'cookies' + os.sep + username
        with open(file_name, mode='wb') as cookies_file:
            pickle.dump(session.cookies, cookies_file)
