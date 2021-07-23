import requests
from urllib3 import disable_warnings

#disable warning for unsafe SSL
disable_warnings()

#setup session
session = requests.session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'
}

#URLs
class urls:
    cas = 'https://cas.gzhu.edu.cn/cas_server/login'
    cas_new = 'https://newcas.gzhu.edu.cn/cas/login?locale=zh_cn'
    sso = 'http://jwxt.gzhu.edu.cn/sso/lyiotlogin'
    mygzhu = 'http://my.gzhu.edu.cn/'
    captcha = 'https://cas.gzhu.edu.cn/cas_server/captcha.jsp'
    jwxt = 'http://jwxt.gzhu.edu.cn/jwglxt/xtgl/index_initMenu.html'
    score = 'http://jwxt.gzhu.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'
    rank = 'http://jwxtbb.gzhu.edu.cn/WebReport/ReportServer?reportlet=gzdx_likai_xscjpm.cpt&__showtoolbar__=true&__cumulatepagenumber__=false'

