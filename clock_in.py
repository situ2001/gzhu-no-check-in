import os
from load_from_cookies import load_from_cookies
import msession
import re
import json
import time
from datetime import datetime

session = msession.session


def clock_in(stu_id, token, chat_id):
    load_from_cookies(stu_id)

    res = session.get('http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start')

    # get csrfToken
    csrfToken = re.findall(r'<meta itemscope="csrfToken" content="(?P<token>.*?)">', res.text)

    # before getting the URL with stepId
    form_get_url = {
        'idc': 'XNYQSB',
        'release': '',
        'csrfToken': csrfToken[0],
        'lang': 'zh'
    }
    res_get_url = session.post('http://yqtb.gzhu.edu.cn/infoplus/interface/start', data=form_get_url)

    # get URL with stepId from response
    url = json.loads(res_get_url.text)['entities'][0]

    # get json
    stepId = re.findall(r'form/(?P<id>.*?)/render', url)
    form = {
        'stepId': stepId,
        'instanceId': '',
        'admin': 'false',
        'rand': '114.514',
        'width': '1536',
        'lang': 'zh',
        'csrfToken': csrfToken[0]
    }
    session.headers.update({'referer': 'http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start'})
    data = session.post(url='http://yqtb.gzhu.edu.cn/infoplus/interface/render', data=form)
    data_json = json.loads(data.text)['entities'][0]

    # get boundField (dummy)
    field = ''
    for key in data_json['fields']:
        field += key
        field += ','
    field = field[:-1]

    form_data = data_json['data']
    
    # add some entries to form
    form_data['fieldJKMsfwlm'] = '1'
    form_data['fieldYZNSFJCHS'] = '0'
    form_data['fieldCNS'] = True

    # convert timestamp to datetime and it will be displayed later
    timestamp = form_data['fieldSQSJ'] + 8 * 3600
    _datetime = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    form = {
        'actionId': '1',
        'formData': json.dumps(form_data),
        'rand': '114.514191981',
        'remark': '',
        'nextUsers': '{}',
        'stepId': stepId,
        'timestamp': str(int(time.time())),
        'boundFields': field,
        'csrfToken': csrfToken[0],
        'lang': 'zh'
    }

    submit = session.post('http://yqtb.gzhu.edu.cn/infoplus/interface/doAction', data=form)

    if '打卡成功' in submit.text:
        print ('打卡成功')
        exit(0)
    else:
        print ('打卡失败')
        exit(1)
