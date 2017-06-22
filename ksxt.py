#coding=utf-8

import urllib2

PR = "http://******.com/Uploadfiles/f64caf6a-1eb0-4ef6-b5d9-1467e62fd10e/MonitoringImg/"


def find_imgs():
    imgset = set()   
    response = urllib2.urlopen(PR)
    html = response.read().encode('utf-8')
    l = html.split('.bmp')
    for i in l:
        imgset.add(i[-37:] + '.bmp')
    return imgset


def down_imgs(imgset):
    count = 1
    for i in imgset:
        response = urllib2.urlopen(PR + i)
        img = response.read()
        print '正在保存第 %d 个文件%s...' % (count,i)
        count += 1
        with open(i,'wb') as f:
            f.write(img)


imgset = find_imgs()

print '发现 %d 个文件' % len(imgset)

down_imgs(imgset)




