from login_new import login_new
from clock_in import clock_in
import os

stu_id = str(os.environ['STUID'])
pwd = str(os.environ['STUPWD'])
token = str(os.environ['TOKEN'])
chat_id = str(os.environ['CHAT_ID'])

login_new(stu_id, pwd)
clock_in(stu_id, token, chat_id)
