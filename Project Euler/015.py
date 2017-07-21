#coding=utf-8

'''
网格路径
从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。


对于20×20方阵来说，这样的路径有多少条？
'''

def fact(n):
    fa = 1
    while n > 1:
        fa *= n
        n -= 1
    return fa

print fact(40)/(fact(40-20)*fact(20))
