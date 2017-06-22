#coding=utf-8

import urllib2
import os

def url_open(url):
    '打开一个url，返回HTML原文'
    #req = urllib2.Request(url)
    #req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
    #response = urllib2.urlopen(req)
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    '从首页网址里取得页面页数，返回总数str'
    html = url_open(url).decode('utf-8')
    a = html.find("current-comment-page")+23
    b = html.find(']',a)
    return html[a:b]
                                       



def find_imgs(url):
    '根据构造的第N页的url，找出该页内所有的图片，返回图片地址列表'
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            s = html[a+9:b+4]
            if s[:4] != 'http':
                s = 'http:' + s
            img_addrs.append(s)
        else:
            b = a + 9 
        a = html.find('img src=',b)

    return img_addrs

def save_imgs(folder,img_addrs):
    '根据图片列表逐个打开url ，写二进制文件，命名是把URL以/分割后取最后一段'
    for e in img_addrs:
        filename = e.split('/')[-1]
        with open(filename,'wb') as f:
            data = url_open(e)
            f.write(data)
        




def download_mm(folder='f:\\OOXX',pages=5):
    #os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'

    page_num = int(get_page(url))
    sum = 0
    for i in range(pages):
        page_num -= i
        page_url = "%s/page-%s#comments" % (url,page_num)
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)
        print '第 %d 个页面 %d 张图片已下载' % (i+1,len(img_addrs))
        sum +=len(img_addrs)
    print '================>%d 张图已下载<================' % sum

if __name__ == '__main__':
    download_mm()
