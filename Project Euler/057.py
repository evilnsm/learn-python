#coding:utf-8

'''
平方根逼近
2的平方根可以用一个无限连分数表示：

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + … ))) = 1.414213…
将连分数计算取前四次迭代展开式分别是：

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666…
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379…

接下来的三个迭代展开式分别是99/70、239/169和577/408，但是直到第八个迭代展开式1393/985，分子的位数第一次超过分母的位数。

在前一千个迭代展开式中，有多少个分数分子的位数多于分母的位数？

'''

def convergent():
    a = 3
    b = 2
    while True:
        a,b =2*b+a, a+b
        yield a,b

g = convergent()
n = 1000
count = 0
while n > 1:
    t = g.next()
    if len(str(t[0])) > len(str(t[1])):
        count += 1
    n -= 1

print count