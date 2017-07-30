#coding:utf-8

'''
整数边长直角三角形

若三边长{a,b,c}均为整数的直角三角形周长为p，当p = 120时，恰好存在三个不同的解：

{20,48,52}, {24,45,51}, {30,40,50}
在所有的p ≤ 1000中，p取何值时有解的数目最多？
'''
from collections import Counter

l = []

for a in xrange(1,500):
    for b in xrange(1,500):
        for c in xrange(1,a+b):
            if a <= b and a+b > c and a+b+c <= 1000 and a*a + b*b == c*c :
                l.append(a+b+c)

print Counter(l).most_common(1)[0][0]
print Counter(l).most_common(1)[0][0] == 840
