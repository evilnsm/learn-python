#coding:utf-8

'''
丢番图方程
考虑如下形式的二次丢番图方程：

x2 – Dy2 = 1
举例而言，当D=13时，x的最小值出现在6492 – 13×1802 = 1。

可以断定，当D是平方数时，这个方程不存在正整数解。

对于D= {2, 3, 5, 6, 7}分别求出x取最小值的解，我们得到：

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

因此，对于所有D ≤ 7，当D=5时x的最小值最大。

对于D ≤ 1000，求使得x的最小值最大的D值。
'''

from math import sqrt
from time import time
a = time()

N = 50
r = {}

for D in range(2,N):
    d = int(sqrt(D))
    if d**2 == D:
        continue
    x = 2
    while True:
        y = int(sqrt((x**2-1) / D))
        if x**2 - D * (y**2) == 1:
            r[D] = x
            break
        x += 1
print max(r, key=r.get)

print time()-a










