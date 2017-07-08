#coding=utf-8
'''
习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出："the end"。


import threading

def list_out(i):
    print i
    
info = [1,2,3,4,55,233]

l = []

for x in range(0,6):
    d = threading.Thread(target = list_out,args = [info[x]])
    d.start()
    l.append(d)

for m in l:
    m.join()

print 'the end'

'''
'''
习题二：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
按：163编码为 gbk其余为 utf-8


import urllib
import threading

def title(url):
	d = urllib.urlopen(url).read().decode('utf-8')
	pos1= d.find('<title>')
	pos2 = d.find('</title>')
	title = d[pos1+7:pos2]
	print  title

l=[]

urlinfo = ['http://www.sohu.com','http://www.baidu.com','http://www.sina.com']

for i in range(0,len(urlinfo)):
	d = threading.Thread(target=title,args=[urlinfo[i]])
	d.start()
	l.append(d)

for m in l:
    m.join()
'''

'''
习题三：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，输出网页的http状态码。
按：200=OK
'''
import urllib
import threading

def title(url):
	d = urllib.urlopen(url)
	print  d.code

l=[]

urlinfo = ['http://www.sohu.com','http://www.baidu.com','http://www.sina.com']

for i in range(0,len(urlinfo)):
	d = threading.Thread(target=title,args=[urlinfo[i]])
	d.start()
	l.append(d)

for m in l:
    m.join()
