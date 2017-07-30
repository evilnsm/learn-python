#coding:utf-8

'''
十进制数585 = 1001001001（二进制表示），因此它在这两种进制下都是回文数。

找出所有小于一百万，且在十进制和二进制下均回文的数，并求它们的和。

（请注意，无论在哪种进制下，回文数均不考虑前导零。）
'''

def is_pa(s):
    l = len(s)
    for i in range(l):
        if s[i] != s[-1-i]:
            return False
        if i == l/2:
            return True
        

sums = 0
for i in xrange(1,1000000):
    if is_pa(str(i)) and is_pa(bin(i)[2:]):
        sums += i

print sums
    
