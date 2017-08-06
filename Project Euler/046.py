#coding:utf-8

'''
克里斯蒂安·哥德巴赫曾经猜想，每个奇合数可以写成一个素数和一个平方的两倍之和。

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

最终这个猜想被推翻了。

最小的不能写成一个素数和一个平方的两倍之和的奇合数是多少？
'''

from math import sqrt

def is_com(n):
    if n <= 5:
        return False
    else:
        for i in xrange(2,int(sqrt(n))+1):
            if n % i == 0:
                return True
        return False

def is_p(n):
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True


n = 1
while True:
    t = 2*n+1
    if is_com(t):
        for i in range(1,int(sqrt(n+1/2))+1):
            a = t - 2*i*i
            if is_p(a):
                break
        else:
            print t
            break
    n += 1
        
