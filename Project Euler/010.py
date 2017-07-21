#coding=utf-8
'''
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

end = 2000000

l = [0,0] + range(2,end+1)

for i in xrange(2,int(math.sqrt(end))+1):
    if l[i]:
        l[i*2::i] = [0] * len(l[i*2::i])

print sum(l)
