#coding=utf-8
import urllib2.request
import urllib
import json

content = input("请输入你想翻译的内容")
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
req = urllib2.request.Request(url)
