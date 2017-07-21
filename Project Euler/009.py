#coding=utf-8

'''
特殊毕达哥拉斯三元组
毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足

a2 + b2 = c2
例如，32 + 42 = 9 + 16 = 25 = 52。

有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc
'''
for a in xrange(1,1000):
    for b in xrange(1,1000):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print a,b,c
            break
    else:
        continue
    break

