from login import login
import msession
import pickle
import os

def load_from_cookies(usrname):
    session = msession.session

    if not os.path.exists('cookies') or not usrname in os.listdir('cookies'):
        print ('No such user, please login first!')
        password = input('Please input the password of {}:'.format(usrname))
        login(usrname, password)

    file_name = 'cookies' + os.sep + usrname
    with open(file_name, 'rb') as cookies:
        session.cookies.update(pickle.load(cookies))