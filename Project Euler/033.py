#coding:utf-8


'''
49/98是一个有趣的分数，因为缺乏经验的数学家可能在约简时错误地认为，等式49/98 = 4/8之所以成立，是因为在分数线上下同时抹除了9的缘故。

我们也会想到，存在诸如30/50 = 3/5这样的平凡解。

这类有趣的分数恰好有四个非平凡的例子，它们的分数值小于1，且分子和分母都是两位数。

将这四个分数的乘积写成最简分数，求此时分母的值。
'''
div = 1  #分子 numerator
den = 1  #分母 denominator

import fractions

for ab in range(11,99):
    a = ab / 10
    b = ab % 10
    if b == 0 or b == a:
        continue
    for j in range(1,10):
        bc = b*10+j
        if ab*j == a * bc:
            div *= a
            den *= j

t = fractions.Fraction(div,den)

print t.denominator

