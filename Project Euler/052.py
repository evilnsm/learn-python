#coding:utf-8

'''
可以看出，125874和它的两倍251748拥有同样的数字，只是排列顺序不同。

有些正整数x满足2x、3x、4x、5x和6x都拥有相同的数字，求其中最小的正整数。
'''
from itertools import permutations

n = 10000
'''
while True:
    s = list(str(n*2))
    l = len(s)
    for j in range(3,7):
        if tuple(str(n*j)) not in permutations(s,l):
            break
    else:
        print n
        break
    n += 1
'''

i = 10000
while True:
    if len(str(i))==len(str(2*i))==len(str(3*i))==len(str(5*i))==len(str(6*i)):
        if set(str(i))==set(str(2*i))==set(str(3*i))==set(str(5*i))==set(str(6*i)):
            print(i)
            break
    i+=1
            
    
    
