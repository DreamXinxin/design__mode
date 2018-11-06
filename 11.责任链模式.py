# -*- coding:utf-8 -*-
"""
责任链模式

     定义:使多个对象有机会处理请求,从而避免请求的发布者和接收者之间的耦合关系,将这些对象连成一条链,并沿着这条链传递该请求,直到有一个对象能处理它为止

     角色:抽象处理者,具体处理者,客户端

     适用场景:有多个对象可以处理一个请求,哪个对象处理由运行时决定

     优点:降低耦合度,一个对象无需知道是其他哪一个对象处理其请求

     缺点:请求不保证被接收,链的末端没有处理或链配置错误
"""

from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handel_leave(self,day):
        pass

class GeneralManagerHandler(Handler):
    def handel_leave(self,day):
        if day < 10:
            print('总经理批准请假%s天'%day)

        else:
            print('不能请假')

class DepartmentManagerHandler(Handler):
    def __init__(self):
        self.successor = GeneralManagerHandler()
    def handel_leave(self,day):
        if day < 7:
            print('部门经理批准请假%s天' % day)
        else:
            print('部门经理无权批假')
            self.successor.handel_leave(day)

class ProjectDirectorHandler(Handler):
    def __init__(self):
        self.successor = DepartmentManagerHandler()
    def handel_leave(self,day):
        if day < 3:
            print('项目经理批准请假%s天' % day)
        else:
            print('项目经理无权批假')
            self.successor.handel_leave(day)

day = 6
h = ProjectDirectorHandler()
h.handel_leave(day)

from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handel_leave(self,day):
        pass

class GeneralManagerHandler(Handler):
    def handel_leave(self,day):
        if day < 10:
            print('总经理批准请假%s天'%day)

        else:
            print('不能请假')

class DepartmentManagerHandler(Handler):
    def __init__(self):
        self.successor = GeneralManagerHandler()
    def handel_leave(self,day):
        if day < 7:
            print('部门经理批准请假%s天' % day)
        else:
            print('部门经理无权批假')
            self.successor.handel_leave(day)

class ProjectDirectorHandler(Handler):
    def __init__(self):
        self.successor = DepartmentManagerHandler()
    def handel_leave(self,day):
        if day < 3:
            print('项目经理批准请假%s天' % day)
        else:
            print('项目经理无权批假')
            self.successor.handel_leave(day)

day = 6
h = ProjectDirectorHandler()
h.handel_leave(day)
