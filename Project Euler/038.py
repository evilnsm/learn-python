#coding:utf-8

'''
将192分别与1、2、3相乘：

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

连接这些乘积，我们得到一个1至9全数字的数192384576。我们称192384576为192和(1,2,3)的连接乘积。

同样地，将9分别与1、2、3、4、5相乘，得到1至9全数字的数918273645，即是9和(1,2,3,4,5)的连接乘积。

对于n > 1，所有某个整数和(1,2, … ,n)的连接乘积所构成的数中，最大的1至9全数字的数是多少？
'''

l = []
for i in xrange(1,9999):
    j = 2
    s = str(i)
    while len(s) < 9 :
        s += str(i * j)
        j += 1
    if len(s) == 9:
        l.append(s)

s_max = 123456789
for i in l:
    if '0' not in i and  len(list(i)) == len(set(i)):
        if int(i) > s_max:
            s_max = int(i)

print s_max
print s_max == 932718654
    

