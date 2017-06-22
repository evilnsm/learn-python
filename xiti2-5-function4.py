#coding=utf-8
'''
1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）

2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
'''
t=[x for x in xrange(1,101)]
# print filter(lambda x : x%2==0,t)


def position_args(a,b,c):
    l=[]
    if isinstance(a,list) and isinstance(b,list) and isinstance(c,list):
        l=a
        l.extend(b)
        l.extend(c)
        return max(l)
    return 'params Err'

def key_args(ls1=[1,2,3],ls2=[1,5,65],ls3=[33,445,22]):
    l=ls1 + ls2 + ls3
    return max(l)


def func3(*kargs):
    l=[]
    for i in kargs:
        if not isinstance(i,list):
           return 'params Err'
        else:
            l += i
    return max(l)


assert position_args([1,2,3],[1,5,65],[33,445,22]) == 445
assert key_args() == 445
assert func3([1,2,3],[1,5,65],[33,445,22]) ==445
