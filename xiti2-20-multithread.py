#coding=utf-8
'''
有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，
每个刷卡机每天一共被刷100次。
账户原有500块。所以当天最后的总账应该为1500
'''

import threading

def swipe():
    global total
    count = 100   
    while count > 0:
        mlock.acquire()
        total += 1
        mlock.release()
        count -= 1

total = 500
l = []
mlock = threading.Lock()

for i in xrange(0,10):
    d = threading.Thread(target = swipe)
    d.start()
    l.append(d)

for li in l:
    li.join()

print total
