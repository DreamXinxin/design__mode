# -*- coding:utf-8 -*-
"""
抽象工厂模式

　  定义:定义一个工厂类接口,让工厂子类来创建一系列相关或相互依赖的对象

     角色:抽象工厂角色,具体工厂角色,抽象产品角色,具体产品角色,客户端

     适用场景:系统要独立于产品的创建和组合时,强调一系列相关产品的对象设计以便进行联合调试时,提供一个产品类库,想隐藏产品的具体实现时

     优点:将客户端与类的具体实现相分离,每个工厂创建了一个完整的产品系列,易于交换产品.有利于产品的一致性

     缺点:难以支持新种类的产品


"""

from abc import abstractmethod, ABCMeta

# ------抽象产品------
class PhoneShell(metaclass=ABCMeta):

    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# ------抽象工厂------
class PhoneFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# ------具体产品------
class SmallShell(PhoneShell):
    def show_shell(self):
        print('小手机壳')

class BigShell(PhoneShell):
    def show_shell(self):
        print('大手机壳')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果机壳')

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print('骁龙CPU')

class MediaTekCPU(CPU):
    def show_cpu(self):
        print('联发科CPU')

class AppleCPU(CPU):
    def show_cpu(self):
        print('苹果CPU')

class Andriod(OS):
    def show_os(self):
        print('安卓系统')

class IOS(OS):
    def show_os(self):
        print('iOS系统')

# ------具体工厂------
class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_os(self):
        return Andriod()

    def make_cpu(self):
        return SnapDragonCPU()

class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_os(self):
        return Andriod()

    def make_cpu(self):
        return MediaTekCPU()

class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_os(self):
        return IOS()

    def make_cpu(self):
        return AppleCPU()

# ------客户端------
class Phone:
    def __init__(self,shell,os,cpu):
        self.shell=shell
        self.os=os
        self.cpu=cpu

    def show_info(self):
        print('手机信息')
        self.cpu.show_cpu()
        self.shell.show_shell()
        self.os.show_os()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(shell,os,cpu)

p1 = make_phone(AppleFactory())
p1.show_info()





