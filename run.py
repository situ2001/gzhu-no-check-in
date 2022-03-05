from login_new import login_new
from clock_in import clock_in

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

MAX_RETRY_COUNT = 2

summary = {}

for id in students:
    print("当前学号:", id)
    login_status = False
    clock_in_status = False
    try:
        print("登录中...")
        count = 1
        login_status = login_new(id, students[id])
        while not login_status and count <= MAX_RETRY_COUNT:
            print("登录失败 重试中 次数:", count)
            login_status = login_new(id, students[id])
            count += 1
        print("打卡中...")
        count = 1
        clock_in_status = clock_in(id)
        while not clock_in_status and count <= MAX_RETRY_COUNT:
            print("打卡失败 重试中 次数:", count)
            clock_in_status = clock_in(id)
            count += 1
    except:
        print("失败了，当前学号", id, "\n")
    summary[id] = (login_status, clock_in_status)

print()
print("总结")
for stu in summary:
    (l, c) = summary[stu]
    print("学号", stu, "登录", l, "打卡", c)
