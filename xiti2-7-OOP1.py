#coding=utf-8
'''
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
'''

class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score_list = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score_list)

zm = Student('zhangming',20,[69,88,100])
lq = Student('liqiang',23,[82,60,99])

assert zm.get_name() == 'zhangming'
assert zm.get_age() == 20
assert zm.get_course() == 100


'''
二：定义一个字典类：dictclass。完成下面的功能：

dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})
'''

class Mydict(dict):

    def del_key(self,key):
        del self[key]

    def get_dict(self,key):
        return self[key] if self.has_key(key) else "not found"
    
    def get_key(self):
        return self.keys()

    def update_dict(self,d2):
        self.update(d2)
        return self

d=Mydict({'a':1,'b':2,'c':3})
d.del_key('a')
print d
print d.get_dict('b')
print d.get_key()
print d.update_dict({'d':4,'e':5})
