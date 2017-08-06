#coding:utf-8

'''
公差为3330的三项等差序列1487、4817、8147在两个方面非常特别：其一，每一项都是素数；其二，两两都是重新排列的关系。

一位素数、两位素数和三位素数都无法构成满足这些性质的数列，但存在另一个由四位素数构成的递增序列也满足这些性质。

将这个数列的三项连接起来得到的12位数是多少？
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

for i in range(1000,10000-3330-3330):
    if is_p(i) and is_p(i+3330) and is_p(i+3330+3330):
        a = set(list(str(i)))
        b = set(list(str(i+3330)))
        c = set(list(str(i+3330+3330)))
        if len(a & b) == len(c) and len(a & c) == len(b) and i != 1487:
            print i*100000000 + (i+3330)*10000 + (i+3330+3330)
