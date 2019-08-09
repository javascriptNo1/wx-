#!usrbinenv python3

import itchat
import threading
import time
from apscheduler.schedulers.background import BlockingScheduler

#产生二维码

itchat.auto_login(hotReload=True,enableCmdQR=True)


#微信昵称获取用户id
#itcaht_user_name = itchat.search_friends(name='40円')[0]['UserName']
#利用send_msg发送消息

#一群终将登上高峰的人！ 新围古教练车群
def heart_beat():
    #定义用户的昵称
    print('调用开始')
    #查找用户的userid
    rooms = itchat.get_chatrooms(update=True)

    if rooms is not None:
       for r in rooms:
           uname = r['UserName']
           NickName = r['NickName']
           #print(uname,NickName)
           if(NickName == '新围古教练车群'):
              itchat.send_msg('@古教练 约明天19:00-20:00练车，谢谢',toUserName=uname)
              print('调用结束，信息发送完成')
              #close;

print('等待调用中')
sched = BlockingScheduler()
job = sched.add_job(heart_beat, 'cron', year=2019,month = time.strftime("%m"),day = time.strftime("%d"),hour = 9,minute = 0,second = 00)
sched.start()
job.remove()
#sched.add_job(heart_beat, 'date', run_date=datetime(2019, 8, 9, 10, 55, 0), args=['text'])