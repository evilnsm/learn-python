#coding=utf-8
'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()
'''

class Listinfo(list):
    def add_key(self,keyname):
        self.append(keyname)
        return self

    def get_key(self,num):
        return self[num]

    def update_list(self,lis):
        self.update(lis)
        return self

    def del_key(self):
        d = self[-1]
        self.pop(-1)
        return d

list_info = Listinfo([44,222,111,333,454,'sss','333'])

list_info.add_key('ddd')
print list_info[-1]

print list_info.del_key()

