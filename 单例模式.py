# -*- coding:utf-8 -*-
"""
定义:保证一个类只有一个实例,并提供一个访问它的全局访问点

适用场景:当一个类只能有一个实例而客户可以从一个众所周知的访问点访问它时

优点:对唯一实例的受控访问,相当于全局变量,但是又可以防止此变量被篡改
"""

class Singleton(object):
    #如果该类已经有了一个实例则直接返回,否则创建一个全局唯一的实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self,name):
        if name:
            self.name = name

a = MyClass('a')
print(a)
print(a.name)

b = MyClass('b')
print(b)
print(b.name)

print(a)
print(a.name)
