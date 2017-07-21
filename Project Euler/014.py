#coding=utf-8
'''
在正整数集上定义如下的迭代序列：

n → n/2 （若n为偶数）
n → 3n + 1 （若n为奇数）

从13开始应用上述规则，我们可以生成如下的序列：

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
可以看出这个序列（从13开始到1结束）共有10项。尽管还没有被证明，但我们普遍认为，从任何数开始最终都能迭代至1（“考拉兹猜想”）。

从小于一百万的哪个数开始，能够生成最长的序列呢？

注： 序列开始生成后允许其中的项超过一百万。
'''
import time

def collatz(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        count += 1
    return count

start = 1000000
max_n = 13
max_l = 10

a=time.time()
while start > 13:
    count = collatz(start)
    if count > max_l:
        max_l = count
        max_n = start
    start -= 1

print max_n,max_l,time.time()-a
