# -*- coding: UTF-8 -*-
print "hello,world" print "haha"第一行
import os
print os.path.isdir(r'/home')
# print os.path.isfile(r'C:\Windows\notepad.exe')

try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})


s = 'am I an unicode?我去取'
print isinstance(s, unicode)
print s

class People(object):
    pass

xiaoming =People()
xiaohong =People()

print xiaoming
print xiaohong
print xiaoming==xiaohong

class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,lambda x,y: cmp(x.name,y.name))  #2. sorted(L1,key = lambda x:x.name)

print L2[0].name
print L2[1].name
print L2[2].name

class Student(object):
    def __init__(self, name, gender, birth, *args, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth

        for i in args:
            self.args[i] = args[i]

        for k,v in kw.items():
            setattr(self, k, v)
haha = Student('Xiao Ming', 'Male', '1990-1-1',job='Student')
print haha.name,haha.birth,haha.job