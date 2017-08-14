#coding:utf-8
'''
由三个4位数8128、2882、8281构成的有序集有如下三个有趣的性质。

这个集合是循环的，每个数的后两位是后一个数的前两位（最后一个数的后两位也是第一个数的前两位）。
每种多边形数——三角形数（P3,127=8128）、正方形数（P4,91=8281）和五边形数（P5,44=2882）——在其中各有一个代表。
这是唯一一个满足上述性质的4位数有序集。
存在唯一一个包含六个4位数的有序循环集，每种多边形数——三角形数、正方形数、五边形数、六边形数、七边形数和八边形数——在其中各有一个代表。求这个集合的元素和。
'''

import sys

l3 = [n*(n+1)/2 for n in range(45,141)]
l4 = [n**2 for n in range(32,99)]
l5 = [n*(3*n-1)/2 for n in range(26,82)]
l6 = [n*(2*n-1) for n in range(23,71)]
l7 = [n*(5*n-3)/2 for n in range(21,64)]
l8 = [n*(3*n-2) for n in range(19,59)]

def link(ls,start,end,found_numbers=[]):
    if len(ls) == 1 and start*100 + end in ls[0]:
        found_numbers.append(start*100 + end)
        found_numbers.append(a)
        print found_numbers,sum(found_numbers)
        sys.exit()
    for l in ls:
        for n in l:
            if n/100 == start:
                ls_copy = ls[:]
                ls_copy.remove(l)
                link(ls_copy,n%100,end,found_numbers + [n])
                #找到一个数后，继续以他的结尾作为开头去连接下一个数，
                #后面还有没有下文其实未知
                #每次的found_numbers都驻留内存
                #直到目标答案出现才强行退出
                #函数认知的区别是没有唯一的返回值


#利用循环去做连线工作，产生一堆长长短短的list
for a in l8:
    link([l3,l4,l5,l6,l7],a%100,a/100)

    
                        
