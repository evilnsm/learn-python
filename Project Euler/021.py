#coding:utf-8
'''
记d(n)为n的所有真因数（小于n且整除n的正整数）之和。
如果d(a) = b且d(b) = a，且a ≠ b，那么a和b构成一个亲和数对，a和b被称为亲和数。

例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和110，因此d(220) = 284；

而284的真因数包括1、2、4、71和142，因此d(284) = 220。

求所有小于10000的亲和数的和。
'''

def d(n):
    m = 0
    for x in xrange(1,n):
        if n%x == 0:
            m += x
    return m

def is_ami(n):
    return d(n) != n and d(d(n)) == n

ami=[n for n in xrange(1,10000) if is_ami(n)]

print sum(ami)
print sum(ami)== 31626

