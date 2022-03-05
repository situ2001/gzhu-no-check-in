from pyquery import PyQuery as pq
from msession import session, urls, cookies_dict
import re
from requests.adapters import HTTPAdapter
from des import strenc


def login_new(username: str, password: str):
    session.cookies.clear()

    res = session.get(urls.cas_new, verify=False)
    lt = re.findall(r'name="lt" value="(.*)"', res.text)

    enc_target = username + password + lt[0]

    result_rsa = strenc(enc_target, '1', '2', '3')

    form = {
        'rsa': result_rsa,
        'ul': str(len(username)),
        'pl': str(len(password)),
        'lt': lt[0],
        'execution': 'e1s1',
        '_eventId': 'submit',
    }

    adapter = HTTPAdapter(max_retries=10)
    session.mount(urls.cas_new, adapter=adapter)
    res = session.post(urls.cas_new, data=form, timeout=30)

    cookies = session.cookies

    # add cookies to dict
    cookies_dict[username] = cookies

    d = pq(res.text)
    err_msg = d("#errormsghide").text()
    if len(err_msg) > 0:
        print(err_msg)
        return False
    else:
        return True
