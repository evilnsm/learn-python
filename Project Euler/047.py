#coding:utf-8

'''
首次出现连续两个数均有两个不同的质因数是在：

14 = 2 × 7
15 = 3 × 5
首次出现连续三个数均有三个不同的质因数是在：

644 = 22 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
首次出现连续四个数均有四个不同的质因数时，其中的第一个数是多少？
'''
from math import sqrt

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

def prime_factors(n):
    l = []
    for i in xrange(2,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
            l.append(n/i)
        if i*i == n:
            l.pop(-1)
    return [x for x in l if is_p(x)]


s = 646
while True:
    if len(prime_factors(s)) == 4 and len(prime_factors(s+1)) == 4 and len(prime_factors(s+2)) == 4 and len(prime_factors(s+3)) == 4:
        print s
        break
    s += 1


