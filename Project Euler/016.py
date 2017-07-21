#coding=utf-8

'''
Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

N = 1000
   
def power_digit_sum(n):
    return sum(map(int,str(int(2 << n-1))))    

print power_digit_sum(N)


#math.pow(2,n) if N>10000,Overflow ~~!
