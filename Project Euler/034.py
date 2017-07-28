#coding:utf-8

'''
145是个有趣的数，因为1! + 4! + 5! = 1 + 24 + 120 = 145。

找出所有各位数字的阶乘和等于其本身的数，并求它们的和。

注意：因为1! = 1和2! = 2不是和的形式，所以它们并不在讨论范围内。
'''

from time import time

a = time()
for i in xrange(11,362880*7):
    m = i
    total = 0
    while m:
        f = 1
        b = m % 10
        for j in range(1,b+1):
            f *= j
        total += f
        m /= 10
    if total == i:
        print i
print time()-a



from math import factorial
a = time()
l_facs = [factorial(x) for x in range(10)]
for i in xrange(11,l_facs[9]*7):
    if i == sum([ l_facs[int(k)] for k in str(i) ]):
        print i
print time()-a
