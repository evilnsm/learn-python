#coding:utf-8

'''
1406357289是一个0至9全数字数，因为它由0到9这十个数字排列而成；但除此之外，它还有一个有趣的性质：子串的可整除性。

记d1是它的第一个数字，d2是第二个数字，依此类推，我们注意到：

d2d3d4=406能被2整除
d3d4d5=063能被3整除
d4d5d6=635能被5整除
d5d6d7=357能被7整除
d6d7d8=572能被11整除
d7d8d9=728能被13整除
d8d9d10=289能被17整除
找出所有满足同样性质的0至9全数字数，并求它们的和。
'''

import itertools

a = list('0123456789')
sums = 0

for p in itertools.permutations(a,10):
    m = "".join(p)
    if int(m) > 999999999 and int(m[1:4])%2==0 and int(m[2:5])%3==0 and int(m[3:6])%5==0 and int(m[4:7])%7==0 \
    and int(m[5:8])%11==0 and int(m[6:9])%13==0 and int(m[7:10])%17==0 :
        sums += int(m)
print sums
