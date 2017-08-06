#coding:utf-8

'''
五边形数由公式Pn=n(3n−1)/2生成。前十个五边形数是：

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, …
可以看出P4 + P7 = 22 + 70 = 92 = P8。然而，它们的差70 − 22 = 48并不是五边形数。

在所有和差均为五边形数的五边形数对Pj和Pk中，找出使D = |Pk − Pj|最小的一对；此时D的值是多少？
'''
#第一次出现符合条件的数就是答案

from math import sqrt

def is_pentagon_num(p):
    n = int((sqrt(6*p + 2.25) + 1.5)/3)
    if n * (3*n-1) == 2*p:
        return True
    return False

N = 10000

l = [x*(3*x-1)/2 for x in range(1,N)]

for i in l:
    for j in l:
        if is_pentagon_num(abs(j-i)) and is_pentagon_num(i+j):
            print j-i
            break
    else:
        continue
    break

