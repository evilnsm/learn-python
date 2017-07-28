#coding:utf-8


'''
如果一个n位数包含了1至n的所有数字恰好一次，我们称它为全数字的；例如，五位数15234就是1至5全数字的。

7254是一个特殊的乘积，因为在等式39 × 186 = 7254中，被乘数、乘数和乘积恰好是1至9全数字的。

找出所有被乘数、乘数和乘积恰好是1至9全数字的乘法等式，并求出这些等式中乘积的和。

注意：有些乘积可能从多个乘法等式中得到，但在求和的时候只计算一次。

'''

l=[]

for i in xrange(1,99):
    for j in xrange(101,9999):
        N = i * j
        if N  > 10000:
            break
        l.append("%s%s%s"%(i,j,N))


c_sum = 0

c = []

for e in l:
    t = list(e)
    t.sort()
    if t == list('123456789'):
        c.append(int(e[-4:]))

print sum(set(c))
