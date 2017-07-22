#coding:utf-8
'''
下列信息是已知的，当然你也不妨自己再验证一下。

1900年1月1日是星期一。

在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是星期天？
'''

year = 1901
count = 0
days = 366

dcomm = [31,28,31,30,31,30,31,31,30,31,30,31]
dleap = [31,29,31,30,31,30,31,31,30,31,30,31]

while year < 2001:
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        d = dleap
    else:
        d = dcomm
    for i in d:
        days += i
        if days%7 == 6:
            count += 1
    year += 1

if days%7 == 6:
    count = count - 1 #d最后一项31加上去后，实际已经到了第二年的1/1，即此处为2001/1/1

print count

            
