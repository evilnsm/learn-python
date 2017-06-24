#coding=utf-8
'''
题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。

'''

import urllib

class myUrl():
    def __init__(self,url):
        self.url = url

    def get_httpcode(self):
        return urllib.urlopen(self.url).code

    def get_htmlcontent(self):
        return urllib.urlopen(self.url).read()

    def get_linknum(self):
        html = self.get_htmlcontent()
        return len(html.split('<a href=')) - 1


url=myUrl('http://www.163.com')
print url.get_httpcode()
print url.get_htmlcontent()
print url.get_linknum()
        
