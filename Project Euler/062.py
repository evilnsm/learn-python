#coding:utf-8
'''
立方数41063625（3453）可以重排为另外两个立方数：56623104（3843）和66430125（4053）。实际上，41063625是重排中恰好有三个立方数的最小立方数。

求重排中恰好有五个立方数的最小立方数。
'''

l = map(sorted,[str(x**3) for x in range(1,10000)])
r = 0
for i in l:
    if l.count(i) >= 5:
        r = l.index(i) + 1
        break
print r**3
 
