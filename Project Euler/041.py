#coding:utf-8

'''
如果一个n位数恰好使用了1至n每个数字各一次，我们就称其为全数字的。例如，2143就是一个4位全数字数，同时它恰好也是一个素数。

最大的全数字的素数是多少？
'''
import itertools
import math

def is_p(n):
    if n == 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,(int(math.sqrt(n))+1)):
            if n % i == 0:
                return False
        return True



pmax = 0
j = 9
while not pmax:
    a = [str(i) for i in range(1,j+1)]
    l = [] 
    for p in itertools.permutations(a,j):
        n = int("".join(p))
        if is_p(n):
            l.append(n)
    if l:
        pmax = max(l)
    j -= 1

print pmax
print pmax == 7652413
