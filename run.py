from login_new import login_new
from clock_in import clock_in

students = {}

with open('stu_id.txt', mode='r') as f:
    for line in f:
        stu = line.split(' ')
        stu = [x.strip() for x in stu]
        students[stu[0]] = stu[1]

for id in students:
    print ('Student loaded: {}'.format(id))

print()
print('开始打卡...')

for id in students:
    login_new(id, students[id])
    clock_in(id)