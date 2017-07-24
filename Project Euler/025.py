#coding:utf-8

def fibs():
    a = 1
    b = 1
    while True:
        a,b = b,a+b
        yield b

f = fibs()
t = 2
N = 1

for i in xrange(1,1000):
    N *= 10

for i in f:
    t += 1
    if i < N:
        continue
    else:
        print i,t
        print t == 4782
        break


    
