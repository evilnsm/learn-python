#coding=utf-8

'''
求10亿以后的100个素数
可以看出时间差主要由于 for...in 循环没有 while 循环快
'''

import time
import math

def is_p(n):
    if not isinstance(n,int):
        raise TypeError
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,(int(math.sqrt(n))+1)):
            if n % i == 0:
                return False
        return True


def find_p():
    begin = 1000000000
    while True:
        if is_p(begin):
            yield begin
        begin += 1



l1=[]
l2=[]
count = 100

#coroutine
a1=time.time()
p = find_p()
for i in range(0,count):
    l1.append(p.next())
b1=time.time()
print l1
print 'coroutine time used: %s s'% (b1-a1)

#loop
a2=time.time()
start=1000000000
while count:
    if is_p(start):
        l2.append(start)
        count -= 1
    start += 1
b2=time.time()
print l2
print 'loop time used: %s s'% (b2-a2)
    
    
    
