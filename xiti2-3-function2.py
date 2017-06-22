#coding=utf-8
#1定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表。
def get_num(num):
    l=[]
    for i in num:
        if not isinstance(i,int):
            print 'ERR'
            return [x for x in num if x%2==0]
    return max(num)

#print get_num([1,5,'a'])

#2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容
import urllib 
def get_page(url='http://www.baidu.com'):
    response = urllib.urlopen(url)
    html = response.read()
    return html.decode('utf-8')

#print get_page()

#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
#理解成：返回每个列表中最大的一个元素组成的列表
def list_max(*ls):
    s=[]
    for l in ls:
        s.append(max(l))
    return s
#print list_max([1,3,5],[7,8,25])


#4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
import os
def get_dir(f):
    ls=os.listdir(f)
    result=[]
    for i in ls:
        if os.path.isdir(f + '\\' + i):
            result.append(i)
    return result if result else 'No dir'

#print get_dir('c:')
print get_dir('f:')

