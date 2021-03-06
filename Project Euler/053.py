#coding:utf-8

'''
从五个数12345中选择三个恰好有十种方式，分别是：

123、124、125、134、135、145、234、235、245和345
在组合数学中，我们记作：5C3 = 10。

一般来说，

nCr=n! / r!(n−r)!，其中r ≤ n，n! = n×(n−1)×…×3×2×1，且0! = 1。

直到n = 23时，才出现了超出一百万的组合数：23C10 = 1144066。

若数值相等形式不同也视为不同，对于1 ≤ n ≤ 100，有多少个组合数nCr超过一百万？
'''


def combinations(n,r):
    mul = 1
    div = 1
    for i in range(1,r+1):
        mul *= (n-i+1)
        div *= i
    return mul/div


count = 0
for n in xrange(1,101):
    for j in xrange(0,n):
        if combinations(n,j) > 1000000:
            count += 1
print count
        
