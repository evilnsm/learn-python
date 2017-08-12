#coding:utf-8

'''
从1开始逆时针螺旋着摆放自然数，我们可以构造出一个边长为7的螺旋数阵。

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
可以发现，所有的奇数平方都在这个螺旋方针的右下对角线上，更有趣的是，在所有对角线上一共有8个素数，比例达到8/13 ≈ 62%。

在这个方阵外面完整地再加上一层，就能构造出一个边长为9的螺旋方阵。如果不断重复这个过程，当对角线上素数的比例第一次低于10%时，螺旋数阵的边长是多少？
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


def gen_list(n):
    p = n**2
    m = n - 1    
    count = 0
    for i in [p-3*m,p-2*m,p-m,p]:
        if is_p(i):
            count += 1
    return p-3*m,p-2*m,p-m,p,count

n = 3
l = [1]
pcount = 0
while True:
    t = gen_list(n)
    for i in range(4):
        l.append(t[i])
    pcount += t[4]
    if float(pcount)/float(2*n-1) < 0.1:
        break
    n += 2

print n
    
