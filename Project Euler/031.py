#coding:utf-8
'''
英国的货币单位包括英镑£和便士p，在流通中的硬币一共有八种：

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)

以下是组成£2的其中一种可行方式：

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

不限定使用的硬币数目，组成£2有多少种不同的方式？
'''
import time

##########################
a = time.time()
count2 = 1
for t12 in range(3):
    for p62 in range(5):
        for p52 in range(11):
            for p42 in range(21):
                for p32 in range(41):
                    for p22 in range(101):
                        for p12 in range(201):
                            M = p12*1 + p22*2 + p32*5 + p42*10 + p52*20 + p62*50 + t12*100
                            if M == 200:
                                count2 += 1
                            if M > 200:
                                break
print count2,time.time()-a



##########################
a = time.time()
count = 1 
for p1 in range(201):
    for p2 in range(101):
        for p3 in range(41):
            for p4 in range(21):
                for p5 in range(11):
                    for p6 in range(5):
                        for t1 in range(3):
                            N = p1*1 + p2*2 + p3*5 + p4*10 + p5*20 + p6*50 + t1*100                            
                            if N == 200:
                                count += 1
                            if N > 200:
                                break
                                

print count,time.time()-a


