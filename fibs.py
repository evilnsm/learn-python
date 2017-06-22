def fibs():
    a=0
    b=1
    while True:
        a,b = b,a+b
        yield a

for i in fibs():
    if i<1000:
        print i
    else:
        break


