#coding:utf-8

'''
197被称为圆周素数，因为将它逐位旋转所得到的数：197/971和719都是素数。

小于100的圆周素数有十三个：2、3、5、7、11、13、17、31、37、71、73、79和97。

小于一百万的圆周素数有多少个？
'''



import time
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

l = []

N = 1000000

for i in xrange(1,N):
    if is_p(i):
        m = str(i)
        n = 0
        den = pow(10,len(m)-1)        
        iold = i
        while n < len(m):
            inew = (iold % den) * 10 + iold / den
            if not is_p(inew):
                break
            n += 1
            iold = inew
        else:
            l.append(i)

print len(l)
