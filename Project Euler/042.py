#coding:utf-8

'''
三角形数序列的第n项由公式tn = 1/2n(n+1)给出；因此前十个三角形数是：

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
将一个单词的每个字母分别转化为其在字母表中的顺序并相加，我们可以计算出一个单词的值。例如，单词SKY的值就是 19 + 11 + 25 = 55 = t10。如果一个单词的值是一个三角形数，我们就称这个单词为三角形单词。

在这个16K的文本文件words.txt （右击并选择“目标另存为……”）中包含有将近两千个常用英文单词，这其中有多少个三角形单词？
'''

l = [x*(x+1)/2 for x in range(1,30)]
with open('042_words.txt','r') as f:
    m = f.read()
t = [s[1:-1] for s in m.split(',')]
y = [sum([ord(s)-64 for s in k]) for k in t]

count = 0
for x in y:
    if x in l:
        count += 1

print count
