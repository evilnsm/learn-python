#coding=utf-8

#筛选法，list到1亿就内存溢出

import math

big=10000000

l=[0,0] + range(2,big+1)

for i in xrange(2,(int(math.sqrt(big))+1)):
    if l[i]:
        l[i+i::i] = [0] * len(l[i+i::i])

print sum(filter(None,l))



'''
约瑟夫环
'''

n = 50
k = 2
p=[x for x in range(1,n+1)]
while(len(p)>1):
    print k,
    del p[k]
    k = (k+2) % len(p)
    print p

print p
