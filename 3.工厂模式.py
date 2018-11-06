# -*- coding:utf-8 -*-
"""
工厂方法模式

     定义:定义一个创建对象的接口(工厂接口),让子类决定实例化哪个接口

     角色:抽象工厂角色,具体工厂角色,抽象产品角色,具体产品角色

     适用场景:需要生产多种,大量复杂对象的时候,需要降低代码耦合度的时候,当系统中的产品类经常需要扩展的时候

     优点:每个具体的产品都对应一个具体工厂,不需要修改工厂类的代码,工厂类可以不知道它所创建的具体的类,隐藏了对象创建的实现细节

     缺点:每增加一个具体的产品类,就必须增加一个相应的工厂类
"""


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # 抽象产品
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    # 具体产品
    def pay(self, money):
        print('使用支付宝支付%s元' % money)


class ApplePay(Payment):
    def pay(self, money):
        print('使用苹果支付支付%s元' % money)


class PaymentFactory(metaclass=ABCMeta):
    # 抽象工厂
    @abstractmethod
    def create_payment(self):
        pass


class AliPayFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        return AliPay()


class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()


af = AliPayFactory()
ali = af.create_payment()
ali.pay(100)


# 如果要新增支付方式
class WechatPay(Payment):
    def pay(self, money):
        print('使用微信支付%s元' % money)


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


w = WechatPayFactory()
wc = w.create_payment()
wc.pay(200)
