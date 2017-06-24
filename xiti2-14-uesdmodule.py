#coding=utf-8

#用time模块获取当前的时间戳.
import time
print u'当前的时间戳是 %s' % time.time()

#用datetime获取当前的日期，例如：2013-03-29
import datetime
today = datetime.date.today()
print u'当前的日期是 %s' % today
#用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27
day2 = today - datetime.timedelta(days=30)
print u'一个月前的日期是 %s' % day2

#用os模块的方法完成ping www.baidu.com 操作。
import os
output = os.popen('ping www.baidu.com')
print output.read()


'''
定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，
列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"。
'''
#递归实现，必须得传入result?
def kuozhan(dirpwd,rslt_set):
    for f in os.listdir(dirpwd):
        fp = os.path.join(dirpwd,f)
        if os.path.isdir(fp):
            kuozhan(fp,rslt_set)
        else:
            #windows中默认用\分割路径，os.path模块中用extsep来标识
            filename = fp.split('\\')[-1]
            #名称中有 . 号的文件才算有后缀名的文件
            if filename.find('.') != -1:
                rslt_set.add(filename.split('.')[-1])
    return list(rslt_set)
print kuozhan('d:\\newbie',set())

#os.walk实现
def kuozhan(dirpwd):
    l=set()
    for root,dirs,files in os.walk(dirpwd):
        for f in files:
            extname = os.path.splitext(f)[1]
            if extname:
                #去掉后缀名开头的.号
                l.add(extname[1:])
    return list(l)
print kuozhan('d:\\newbie')

'''
定义一个函数xulie(dirname,info) 参数：dirname:路径名，info:需要序列化的数据，
功能：将info数据序列化存储到dirname路径下随机的文件里。
'''
import pickle
import random
def xulie(dirname,info='I love python'):
    if not os.path.isdir(dirname):
        return u'%s is not a valid directory'
    fn = 'test_%s.pkl' % random.randint(1,100)
    ffn = os.path.join(dirname,fn)
    with open(ffn,'w') as f:
        pickle.dump(info,f)
    return ffn
#print xulie('f:\\')
