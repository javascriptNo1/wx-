#!usrbinenv python3

import itchat
import threading
from apscheduler.schedulers.background import BlockingScheduler

#产生二维码

itchat.auto_login(hotReload=True,enableCmdQR=True)


#微信昵称获取用户id
#itcaht_user_name = itchat.search_friends(name='40円')[0]['UserName']
#利用send_msg发送消息

#坤元驾校龙一分部刘教约车群
def heart_beat():
    #定义用户的昵称
    print('定时调用')
    #查找用户的userid
    rooms = itchat.get_chatrooms(update=True)

    if rooms is not None:
       for r in rooms:
           uname = r['UserName']
           NickName = r['NickName']
           #print(uname,NickName)
           if(NickName == '一群终将登上高峰的人！'):
              itchat.send_msg('下班啦！',toUserName=uname)
              close;

sched = BlockingScheduler()
job = sched.add_job(heart_beat, 'cron', year=2019,month = time.strftime("%m"),day = time.strftime("%d"),hour = 18,minute = 15,second = 00)
sched.start()
job.remove()
#sched.add_job(heart_beat, 'date', run_date=datetime(2019, 6, 1, 16, 31, 0), args=['text'])