#coding=utf-8
'''
定义一个生成器函数，函数里只能用yield，要求输出结果：
step 1
step 2 x=haha
step 3 y=haha
提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。
send()方法传入的参数是"haha"
'''

#无论是send还是next，只要调用，都会执行yield

def step():
    x = yield 'step 1'
    y = yield 'step 2 x=%s'%x
    yield 'step 3 y=%s'%y


t=step()

print t.next()
print t.send('haha')
print t.send('haha')


def fibs():
    a = 0
    b = 1
    while True:
        a,b = a+b,a
        yield a

f = fibs()

for i in range(0,36):
    print f.next()

    
