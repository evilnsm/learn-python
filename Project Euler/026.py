#coding:utf-8

'''
单位分数指分子为1的分数。分母为2至10的单位分数的十进制表示如下所示：

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1

这里0.1(6)表示0.166666…，括号内表示有一位循环节。可以看出，1/7有六位循环节。

找出正整数d < 1000，其倒数的十进制表示小数部分有最长的循环节。
'''

def cycles(n):
    if n%2 == 0:
        return cycles(n/2)
    if n%5 == 0:
        return cycles(n/5)
    i = 1    
    while True:
        if  (pow(10,i)-1)%n == 0:
            return i
        else:
            i += 1

l = 0
n = 0
for i in range(2,1000):
    if cycles(i) > l:
        l = cycles(i)
        n = i
        
print n
print n == 983
