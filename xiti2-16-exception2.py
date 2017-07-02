#coding=utf-8

'''
1定义一个函数func(filename) filename:为文件名，用with实现打开文件，并且输出文件内容。
'''
def open_file(filename):
    with open(filename) as f:
        ct = f.read()
    return ct


'''
定好一个函数func(listinfo) listinfo:为列表，
listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555]
返回一个列表包含小于100的偶数，并且用assert来断言
返回结果和类型。
'''

def filter_ls(listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555]):
    return filter(lambda x:x%2==0 and x<100 ,listinfo)

assert type(filter_ls()) == list
assert filter_ls() == [88, 22, 44, 44, 22, 66]



'''
自己定义一个异常类，继承Exception类,
捕获下面的过程：判断raw_input()输入的字符串长度是否小于5，
如果小于5，比如输入
长度为3则输出:" The input is of length 3,expecting at least 5'，
大于5输出"print success'
'''
class my_error(Exception):  
    def __init__(self, stri):  
        self.leng = len(stri)  
    def process(self):  
        if self.leng < 5:  
            return 'The input is of length %s,expecting at least 5' % self.leng  
        else:  
            return 'print success'  
  
try:
    #人为抛异常
    raise my_error(raw_input(u'请输入：'))  
except my_error as e:  
    print e.process() 
