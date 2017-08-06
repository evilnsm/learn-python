#coding:utf-8

'''
十项的自幂级数求和为 11 + 22 + 33 + … + 1010 = 10405071317。

求如下一千项的自幂级数求和的最后10位数字：11 + 22 + 33 + … + 10001000。
'''

def self_pow(n):
    t = 1
    if n % 10 == 0:
        return 0
    for i in range(1,n+1):
        t *= n
        if t >= 10**10:
            t = t % 10**10
    return t

sums = 0
for i in xrange(1,1001):
    sums += self_pow(i)

print sums % 10**10


###############
sums = 0
for i in range(1,1001):
        sums +=i**i
print sums % 10**10
