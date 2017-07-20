#coding=utf-8
'''
最大回文乘积
回文数就是从前往后和从后往前读都一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。

找出由两个3位数相乘得到的最大回文乘积。
'''
b_min = 100 * 100
b_max = 999 * 999

nlist = []

def is_pa(s):
    l = len(s)
    for i in range(0,l):
        if s[i] != s[-1-i]:
            return False
        if i == l/2:
            return True

for x in xrange(b_min,b_max):
    nstr = str(x)
    if is_pa(nstr):
        nlist.append(int(nstr))

nlist.sort(reverse = True)

for n in nlist:
    for j in xrange(999,99,-1):
        m = n/j
        if n % j == 0 and m<=999 and m >= 100:
            print 'the largest palindrome is %s = %s * %s' %(n,j,m)
            break
    else:
        continue
    break

'''
Python的循环体自己就有else分支！
Python的循环体自己就有else分支！
Python的循环体自己就有else分支！
不只是if有，while和for都有else分支。
循环体的else分支触发条件是循环正常结束。
如果循环内被break跳出，就不执行else。所以这个逻辑是：

如果循环内break了，不触发else，则执行下一句外层循环中的break；
如果正常结束，执行else分支里的continue，直接跳转到外层循环的下一轮，跳过了第二个break。

作者：Coldwings
链接：https://www.zhihu.com/question/37076998/answer/70307714
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


