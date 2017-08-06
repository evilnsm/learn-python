#coding:utf-8

'''
三角形数、五边形数和六角形数分别由以下公式给出：

 	 	 
三角形数	Tn=n(n+1)/2	1, 3, 6, 10, 15, …
五边形数	Pn=n(3n−1)/2	1, 5, 12, 22, 35, …
六边形数	Hn=n(2n−1)	1, 6, 15, 28, 45, …
可以验证，T285 = P165 = H143 = 40755。

找出下一个同时是三角形数、五边形数和六角形数的数。
'''

from math import sqrt

def is_pentagon_num(p):
    n = int((sqrt(6*p + 2.25) + 1.5)/3)
    if n * (3*n-1) == 2*p:
        return True
    return False

def is_triangle_num(t):
    n = int(sqrt(2*t + 0.25) - 0.5)
    if n * (n+1) == 2*t:
        return True
    return False

start = 144
while True:
    h = start * (2*start - 1)
    if is_triangle_num(h) and is_pentagon_num(h):
        print h
        print h == 1533776805
        break
    start += 1
