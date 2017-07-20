#coding=utf-8

'''
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
import time

def is_p(n):
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,(int(math.sqrt(n))+1)):
            if n % i == 0:
                return False
        return True

def largest_factor(n):
    l_f = 1
    for i in xrange(2,int(math.sqrt(n))+1):
        if n % i == 0 and is_p(i):
            l_f = i
    return l_f

a=time.time()
print largest_factor(600851475143),time.time()-a



def recur_factors(n):
    for i in xrange(2,int(math.sqrt(n))+1):
        if i == int(math.sqrt(n)): 
            return i if i*i==n else n  #特殊情况是最后一次求解的是个平方数
        elif n % i == 0:
            return recur_factors(n/i)

a=time.time()
print recur_factors(600851475143),time.time()-a





