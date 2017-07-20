#coding=utf-8

'''
平方的和与和的平方之差
前十个自然数的平方的和是

12 + 22 + … + 102 = 385
前十个自然数的和的平方是

(1 + 2 + … + 10)2 = 55~2 = 3025
因此前十个自然数的平方的和与和的平方之差是 3025 − 385 = 2640。

求前一百个自然数的平方的和与和的平方之差。

'''

import time

N=10000000

a=time.time()
sum1 = sum([x*x for x in range(1,N+1)])
sum2 = sum([x for x in range(1,N+1)])

print sum2*sum2 - sum1 , time.time()-a



'''
e1 = n(n+1)(2n+1)/6
e2 = n(n+1)/2
e2*e2 - e1 = (n-1)n(n+1)(3n+2)/12
'''

a=time.time()
print (N-1)*N*(N+1)*(3*N+2)/12, time.time()-a

