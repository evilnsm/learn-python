#coding:utf-8

'''
一古戈尔（10100）是一个巨大的数字：一后面跟着一百个零。100100则更是无法想像地巨大：一后面跟着两百个零。然而，尽管这两个数如此巨大，各位数字和却都只有1。

若a, b < 100，所有能表示为ab的自然数中，最大的各位数字和是多少？
'''

d_max = 0
for a in range(1,100):
    for b in range(1,100):
        p = sum([ord(x)-48 for x in str(a**b)])
        if p > d_max:
            d_max = p
print d_max
