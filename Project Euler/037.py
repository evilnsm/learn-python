#coding:utf-8

'''
3797有着奇特的性质。不仅它本身是一个素数，而且如果从左往右逐一截去数字，剩下的仍然都是素数：3797、797、97和7；同样地，如果从右往左逐一截去数字，剩下的也依然都是素数：3797、379、37和3。

只有11个素数，无论从左往右还是从右往左逐一截去数字，剩下的仍然都是素数，求这些数的和。

注意：2、3、5和7不被视为可截素数。
'''

import math

def is_p(n):
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,(int(math.sqrt(n))+1)):
            if n % i == 0:
                return False
        return True


def is_truncatable(n):
    m = str(n)
    l = len(m)
    pos = 0
    while pos < l:
        if not is_p(int(m[pos:])):
            return False
        pos += 1
    while pos > 0:
        if not is_p(int(m[0:pos])):
            return False
        pos -= 1
    return True

count = 0
sums = 0
i = 8
while count < 11:
    if is_p(i) and is_truncatable(i):
        sums += i
        count += 1
    i += 1

print sums
print sums == 748317



    
