#coding=utf-8

#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def get_fundoc(func):
    if type(func) is FunctionType:
        doc = func.__doc__
        return doc if doc else 'not found'
    else:
        return 'Not Function'

#print get_fundoc(list)


#2.定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
def get_cjsum():
    cjsum = 0
    for i in range(1,101):
        cjsum += i*i
    return cjsum
#其实一行就可以，用带生成器的推导式
    #return sum(i*i for i in range(1,101))
print get_cjsum()




#4.定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，
import os.path as o

def get_funcname(func):
    if callable(func):
        name = func.__code__.co_name
        return name if name else 'not found'
    else:
        return 'Not Function'


#可以取得
assert get_funcname(get_cjsum) == 'get_cjsum'
#不可以
print get_funcname(o.isdir)

