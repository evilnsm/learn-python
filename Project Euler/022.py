#coding:utf-8
'''
在这个46K的文本文件names.txt中包含了五千多个姓名。首先将它们按照字母序排列，然后计算出每个姓名的字母值，乘以它在按字母顺序排列后的位置，以计算出姓名得分。

例如，按照字母序排列后，位于第938位的姓名COLIN的字母值是3 + 15 + 12 + 9 + 14 = 53。因此，COLIN的姓名得分是938 × 53 = 49714。

文件中所有姓名的姓名得分之和是多少？
'''

def score(name): 
    return sum(map(lambda x:ord(x)-64,name))

with open('022_names.txt','r') as f:
    rr = f.readlines()

l = [s.replace('"','') for s in rr[0].split(',')]
l.sort()
s = [score(x)*(l.index(x)+1) for x in l]

print sum(s)
print sum(s) == 871198282

