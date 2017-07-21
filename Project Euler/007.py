#coding=utf-8
'''
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math

def is_prime(n):
    if n== 1:
        return False
    elif n == 2:
    	return True
    else:
        for i in xrange(2,(int(math.sqrt(n))+1)):
            if n % i == 0:
                return False
        return True


def find_prime():
    begin = 0
    count = 0
    while count < 10001:    
        begin += 1
        if is_prime(begin):
            count += 1
    return begin

print find_prime()
