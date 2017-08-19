#coding=utf-8

'''
幂次与位数

五位数16807=7**5同时也是一个五次幂。同样的，九位数134217728=8**9同时也是九次幂。

有多少个n位正整数同时也是n次幂？
'''
count = 0
for i in range(1,10):
    for j in range(1,100):
        p = i**j
        if len(str(p)) == j:
            count += 1

print count
