#coding:utf-8
'''
欧拉发现了这个著名的二次多项式：

n2 + n + 41
对于连续的整数n从0到39，这个二次多项式生成了40个素数。然而，当n = 40时，402 + 40 + 41 = 40(40 + 1) + 41能够被41整除，同时显然当n = 41时，412 + 41 + 41也能被41整除。

随后，另一个神奇的多项式n2 − 79n + 1601被发现了，对于连续的整数n从0到79，它生成了80个素数。这个多项式的系数-79和1601的乘积为-126479。

考虑以下形式的二次多项式：

n2 + an + b, 满足|a| < 1000且|b| < 1000

其中|n|指n的模或绝对值
例如|11| = 11以及|−4| = 4

这其中存在某个二次多项式能够对从0开始尽可能多的连续整数n都生成素数，求其系数a和b的乘积。
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

r={}

for a in range(-999,1000):
    for b in range(-999,1000):
        i = 0
        while True:
            N = i*i + a*i + b
            if N>0 and is_p(N):
                i += 1
            else:
                break
        if i > 39: #已知条件里至少有40个
            r[(a,b)] = i

count = 39
p = 1*41

for k,v in r.items():
    if v >= count:
        count = v
        p = k[0] * k[1]

print p
print p == -59231
    
