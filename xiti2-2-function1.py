# -*- coding:utf-8 -*-

import urllib
import glob

#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def funcfind(*arr):
    for i in arr:
        if not isinstance(i,int):
            return 'ERR'
    l=list(arr)
    l.sort()
    return l[-1],l[0]

#print funcfind(1,3,5,6,7)
#print funcfind(1,3,5,6,'1')

#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def funclen(*arr):
    for i in arr:
        if not isinstance(i,str):
            return 'ERR'
    r = arr[0]
    for x in arr:
        if len(x) > len(r):
            r = x
    return r

#print funclen('aaa','bsdbsb','gverafer')
#print funclen('aaa','bsdbsb','gverafer',6)

#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
def get_doc(module):
    return module.__doc__

#print get_doc(urllib)

#4.4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f):
    with open(f,'rb') as g:
        return g.read()

#print get_text('c:\SmartChange.bat')

#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
def get_dir(folder):
    return glob.glob(folder + '\*.*')

#print get_dir('c:')
