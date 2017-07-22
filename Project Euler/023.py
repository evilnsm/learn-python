#coding:utf-8

'''
完全数是指真因数之和等于自身的那些数。例如，28的真因数之和为1 + 2 + 4 + 7 + 14 = 28，因此28是一个完全数。

一个数n被称为亏数，如果它的真因数之和小于n；反之则被称为盈数。

由于12是最小的盈数，它的真因数之和为1 + 2 + 3 + 4 + 6 = 16，所以最小的能够表示成两个盈数之和的数是24。通过数学分析可以得出，所有大于28123的数都可以被写成两个盈数的和；尽管我们知道最大的不能被写成两个盈数的和的数要小于这个值，但这是通过分析所能得到的最好上界。

找出所有不能被写成两个盈数之和的正整数，并求它们的和。
'''

import math

def is_abundant(n):
    d = 1
    for x in xrange(2,int(math.sqrt(n))+1):
        if n%x == 0:
            d += (x + n/x)
    if x*x == n:
        d -= x
    return d > n

ab = [x for x in xrange(12,28123-11) if is_abundant(x)]

absum = set([x+y for x in ab for y in ab if x+y < 28123])

non_absum = 0

for n in xrange(1,28123):
    if n not in absum:
        non_absum += n

print non_absum
