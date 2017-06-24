#coding=utf-8

import urlparse

def qs(url):
    querystring = urlparse.urlparse(url).query
    l = [(k,v[0]) for k,v in urlparse.parse_qs(querystring).items()]
    return dict(l)

print qs('http://126.com')
print qs('http://api/api?f=5&g=6&y=5')
print qs('http://api/api?11=53')
