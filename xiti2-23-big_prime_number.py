#coding=utf-8

import time

def is_p(n):
    if not isinstance(n,int):
        raise TypeError
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True



'''
l = [x for x in xrange(100,200) if is_p(x)]
print l
'''

'''
结果很神奇,count = 10时，协程1.99s 循环1.94s
count=100时，协程17.27s 循环17.39s
count=1000时，协程177.45s 循环177.89s
'''

def find_p():
    begin = 1000000
    while True:
        if is_p(begin):
            yield begin
        begin += 1



l1=[]
l2=[]
count = 1000

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
start=1000000
while count:
    if is_p(start):
        l2.append(start)
        count -= 1
    start += 1
b2=time.time()
print l2
print 'loop time used: %s s'% (b2-a2)
    
    
    
