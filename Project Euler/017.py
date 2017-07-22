#coding=utf-8

'''

如果把1到5写成英文单词，分别是：one, two, three, four, five，这些单词一共用了3 + 3 + 5 + 4 + 4 = 19个字母。

如果把1到1000都写成英文单词，一共要用多少个字母？

注意： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含23个字母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式英语的规则。
'''

digits=['one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine']
teens=['ten',
       'eleven',
       'twelve',
       'thirteen',
       'fourteen',
       'fifteen',
       'sixteen',
       'seventeen',
       'eighteen',
       'nineteen',
       'twenty']
tens=['twenty',
      'thirty',
      'forty',
      'fifty',
      'sixty',
      'seventy',
      'eighty',
      'ninety']

#1~20
count1 = sum([len(x) for x in digits + teens])
count1 *= 10

#21-99
s = ["%s%s" % (x,y) for x in tens for y in digits] + tens[1:]
count2 = sum([len(x) for x in s])
count2 *= 10

#100/.../900
count3 = sum([len(x) for x in digits]) + len('hundred') * 9
count3 *= 100

#and
count4 = len('and') * 99 * 9

print count1+count2+count3+count4+len('onethousand')

############
d = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
c = []

for i in xrange(1,1000):
    if 1 <= i <= 20:
        m = d[i]
    elif 21 <= i <= 99:
        if i%10 == 0:
            m = d[i]
        else:
            m = d[int(i/10)*10] + d[i%10]
            d[i] = m
    else:
        if i%100 == 0:
            m = d[i/100] + len('hundred')
        else:
            m = d[int(i/100)] + len('hundredand') + d[i%100]
    c.append(m)

print sum(c) + len('onethousand')
        




