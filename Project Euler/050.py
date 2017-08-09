#coding:utf-8

'''
素数41可以写成六个连续素数的和：

41 = 2 + 3 + 5 + 7 + 11 + 13
在小于一百的素数中，41能够被写成最多的连续素数的和。

在小于一千的素数中，953能够被写成最多的连续素数的和，共包含连续21个素数。

在小于一百万的素数中，哪个素数能够被写成最多的连续素数的和？
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

N=1000000

l = [x for x in range(1,N) if is_p(x)]

length = 21
j = 0
r = [[] for i in range(527)]
for length in range(21,547):
    for i in range(527):
        if i + length < 547:
            n = sum(l[i:i+length])
            if n < N and is_p(n):
                r[j].append(n)
    j += 1

print str(max(r))[1:-1]

###############################
maxlong = 547
while True:
    pos = 0
    while pos + maxlong < len(l):
        n = sum(l[pos:pos + maxlong])
        if n > N:
            break
        elif n < N and is_p(n):
            print n
            exit()
        pos += 1
    maxlong -= 1


