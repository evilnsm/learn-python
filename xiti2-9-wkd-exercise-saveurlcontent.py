#coding=utf-8
import urllib
import os
import random

def save_url_content(url,folder='f:\\'):
    if not (url.startswith('http://') or url.startswith('https://')):
        return u'url地址不正确'
    if not os.path.isdir(folder):
        return u'%s非文件夹' % folder
    try:
        response = urllib.urlopen(url)
        content = response.read()
    except:
        content = '网络故障，失去响应'
    #filename
    fn = 'test%8d.txt' % random.randint(10000000,90000000)
    #file_full_path_name
    ffn = os.path.join(folder,fn)
    with open(ffn,'w') as f:
        f.write(content)
    return ffn

print save_url_content('http://www.baidu.com')


def get_links_count(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        return u'url地址不正确'
    try:
        response = urllib.urlopen(url)
        content = response.read()
    except:
        content = ''
    return len(content.split('<a href=')) - 1

print get_links_count('http://10.78.214.168')
