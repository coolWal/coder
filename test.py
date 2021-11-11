# class Borg(object):
#     __shared_state = {"1":"2"}
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state

# class Borg(object):
#     __shared_state = {}
#     def __new__(cls, *args, **kwargs):
#         obj = super(Borg, cls).__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls.__shared_state
#         return obj


# b = Borg()
# b1 = Borg()
# b.x = 5
# b.r = "a"

# print(b)
# print(b1)
# print(b.__dict__)
# print(b1.__dict__)

# class MetaSingleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in _instances:
#             cls._instances[cls] = super(metasingleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

# # class Logger(metaclass=metaSingleton):
# #     pass

# class Database(metaclass=MetaSingleton):
#     connection = None
#     def connection(self):
#         if self.connection is None:
#             self.connection = sqlite3.connect("db.sqllte3")
#             self.cursorobj = self.connection.cursor()
#         return self.cursorobj

# class HealthCheck(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not HealthCheck._instance:
#             HealthCheck._instance = object.__new__(cls, *args, **kwargs)
#         return HealthCheck._instance

#     def __init__(self):
#         self._servers = []
    
#     def add_server(self):
#         self._servers.append("Server 1")
#         self._servers.append("Server 2")
#         self._servers.append("Server 3")
#         self._servers.append("Server 4")
#         self._servers.append("Server 5")
#         self._servers.append("Server 6")

#     def change_server(self):
#         self._servers.pop()
#         self._servers.append("Server 7")

# #简单工厂模式
# from abc import ABCMeta, abstractmethod

# class Animal(metaclass=ABCMeta):
    
#     @abstractmethod
#     def do_say(self):
#         pass


# class Dog(Animal):
#     def do_say(self):
#         print("aaa")

# class Cat(Animal):
#     def do_say(self):
#         print("vbbbb")

# class Factory(object):
#     def make_sound(self, object_type):
#         return eval(object_type)().do_say()

# 工厂方法模式
# from abc import ABCMeta, abstractmethod

# class Section(metaclass=ABCMeta):
#     @abstractmethod
#     def describe(self):
#         pass

# class PersonalSection(Section):
#     def describe(self):
#         print("Personal Section")

# class AlbumSection(Section):
#     def describe(self):
#         print("Album Section")
    
# class PatentSection(Section):
#     def describe(self):
#         print("Patent Section")

# class PublictionSection(Section):
#     def describe(self):
#         print("publiction Section")

# class Profile(object):
#     def __init__(self):
#         self.sections = []
#         self.create_profile()

#     @abstractmethod
#     def create_profile(self):
#         pass

#     def get_sections(self):
#         return self.sections
    
#     def add_sections(self, section):
#         self.sections.append(section)
    
# class Linkedin(Profile):
#     def create_profile(self):
#         self.add_sections(PersonalSection)
#         self.add_sections(PatentSection)
#         self.add_sections(PublictionSection)

# class Facebook(Profile):
#     def create_profile(self):
#         self.add_sections(PersonalSection)
#         self.add_sections(AlbumSection)

# # 抽象工厂模式
# from abc import ABCMeta, abstractmethod

# class PizzaFactory(metaclass=ABCMeta):

#     @abstractmethod
#     def createVegPizza(self):
#         pass

#     @abstractmethod
#     def createNonVegPizza(self):
#         pass

# class IndianPizzaFactory(PizzaFactory):
    
#     def createVegPizza(self):
#         return DeluxVeggiePizza()

#     def createNonVegPizza(self):
#         return ChickenPizza()


# class USPizzaFactory(PizzaFactory):

#     def createVegPizza(self):
#         return MexicanVegPizza()

#     def createNonVegPizza(self):
#         return HamPizza()

# class VegPizza(metaclass=ABCMeta):

#     @abstractmethod
#     def prepare(self, VegPizza):
#         pass

# class NonVegPizza(metaclass=ABCMeta):
#     @abstractmethod
#     def serve(self):
#         pass

# class DeluxVeggiePizza(VegPizza):
    
#     def prepare(self):
#         print("prepare")

# class ChickenPizza(NonVegPizza):

#     def serve(self, VegPizza):
#         print("serve", VegPizza)

# class MexicanVegPizza(VegPizza):
    
#     def prepare(self): 
#         print("prepare")

# class HamPizza(NonVegPizza):

#     def serve(self, VegPizza):
#         print("prepare", type(VegPizza).__name__)

# class PizzaStory(object):
#     def __init__(self):
#         pass

#     def make_pizzas(self):
#         for factory in [USPizzaFactory()]:
#             self.factory = factory
#             self.NovVegPizza = self.factory.createNonVegPizza()
#             self.VegPizza = self.factory.createVegPizza()
#             self.VegPizza.prepare()
#             self.NovVegPizza.serve(self.VegPizza)

# # 门面模式
# class EventManager(object):

#     def __init__(self):
#         print("event manager")

#     def arrange(self):
#         self.hotelier = Hotelier()
#         self.hotelier.bookHotel()

#         self.florist = Florist()
#         self.florist.setFlowerRequirements()

#         self.caterer = Caterer()
#         self.caterer.setCuisine()

#         self.musician = Musician()
#         self.musician.setMusicType()

# class Hotelier(object):
#     def __init__(self):
#         print("array arrived!")

#     def bookHotel(self):
#         pass

# class Florist(object):
#     def bookHotel(self):
#         print("book hotel")

#     def setFlowerRequirements(self):
#         pass

# class Caterer(object):
#     def setFlowerRequirements():
#         print("set flower require ments")

#     def setCuisine(self):
#         pass

# class Musician(object):
#     def setMusicType(self):
#         print("set music type")

# class Your(object):
#     def __init__(self):
#         print("You whoa!")

#     def askEventManager(self):
#         print("You: Let's Contact the Event")
#         em = EventManager()
#         em.arrange()

#     def __del__(self):
#         print("you del！")

# class Test:
#     def __del__(self):
#         print("exit")

# 代理模式
from abc import ABCMeta, abstractmethod
import abc
from types import MethodWrapperType
from typing import Sequence

from sqlite3.dbapi2 import Date

class You(object):
    def __init__(self):
        self.debitCard = DebitCard()
        self.ispurchased = None

    def make_payment(self):
        self.ispurchased =  self.debitCard.do_pay()
    
    def __del__(self):
        if self.ispurchased:
            print("yes")
        else:
            print("no")

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            return True
        else:
            return False

class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input()
        self.bank.setCard(card)
        return self.bank.do_pay()

# LocalProxy代理
from functools import partial
from werkzeug.local import LocalProxy

class Boss(object):

    def pop(self):
        print("ok")
        return "ok"

# 观察者模式
class OtherObj(object):

    def __init__(self, Obj):
        self.real_obj = Obj()

other = OtherObj(Boss)

def get_boss(obj=None):
    return obj.real_obj

proxy_boss = LocalProxy(partial(get_boss, other))

class Subject(object):

    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__)

class Observer2(object):
    def __init__(self, subject):     
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__)

from abc import abstractmethod

# 主题
class NewPublisher:
    
    def __init__(self):
        self.__subscribers = list()
        self.__latestNews = None

    def attach(self, subscribers):
        self.__subscribers.append(subscribers)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latestNews = news

    def get_news(self):
        return self.__latestNews

# 观察者
class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

# 具体观察者

class SMSSubscriber(object):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.get_news())

class EmailSubscirber(object):
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())

class Wizard(object):
    def __init__(self, rootdir, src):
        self.choices = []
        self.rootdir = rootdir
        self.src =  src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print(self.rootdir)

            else:
                print("no")

# 命令模式
from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    
    @abstractmethod
    def excute(self):
        pass

class BuyStockOrder(Order):

    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def excute(self, stock):
        self.stock.sell()

class StockTrade(object):
    def buy(self):
        print("you will buy stocks")

    def sell(self):
        print("you will sell stocks")

class Agent(object):

    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

# mvc模型
# class Model(object):

#     services = {
#         "email":{"number":1000, "price": 2},
#         "sms": {"number": 1000, "price": 10},
#         "voice": {"number": 1000, "price": 15}
#     }

# class View(object):

#     def list_services(self, services):
#         for svc in services:
#             print(svc)

#     def list_pricing(self, services):
#         for svc in services:
#             print(svc)


# class Controller(object):

#     def __init__(self):
#         self.model = Model()
#         self.view = View()

#     def get_services(self):
#         services = self.model.services.keys()
#         return self.view.list_services(services)

#     def get_pricing(self):
#         priceing = self.model.services.keys()
#         return self.view.list_pricing(priceing)


# class Client(object):
#     controller = Controller()
#     controller.get_services()
#     controller.get_pricing()


class Model(object):
    def logic(self):
        data = "Got it!"
        return Date

class View(object):
    def update(self, data):
        print("data", data)

class Controller(object):

    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        data = self.model.logic()
        self.view.update(data)

class Client(object):
    controller = Controller()
    controller.interface()


import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

# 模型
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")
    
class NewHandler(tornado.web.RequestHandler):
    def post(self):
        pass

class UpdateHandler(tornado.web.RequestHandler):
    
    def get(self):
        pass

class RunApp(tornado.web.Application):
    # 控制器
    def __init__(self):
        Handlers = [
            (r"/", IndexHandler),
            (r"/new", NewHandler),
            (r"/update", UpdateHandler),
        ]
        settings = dict(
            debug=True
        )
        tornado.web.Application.__init__(self, Handlers, **settings)


from abc import abstractclassmethod, ABCMeta

class State(metaclass=ABCMeta):

    @abstractclassmethod
    def Handler(self):
        pass

class ConcreteStateB(State):

    def Handler(self):
        print("ConcreateStateB")

class ConcreteStateA(State):

    def Handler(self):
        print("ConcreteStateA")

class Context(State):

    def __init__(self):
        self.state = None

    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state

    def Handler(self):
        self.state.Handler()

class ComputerState(object):
    name="state"
    allowed=[]  

    def switch(self, state):
        if state.name in self.allowed:
            print("cureent", self, state.name)

            self.__class__ = state

        else:
            print(self, state.name)

    def __str__(self):
        return self.name

class Off(ComputerState):
    name = 'off'
    allowed = ["on"]

class On(ComputerState):
    name = 'on'
    allowd = ['off', 'suspend', 'hibernate']

class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']

class Computer(object):
    def __init__(self, model='HP'):
        self.model = model 
        self.state = Off()

    def change(self, state):
        self.state.switch(state)

# 模板方法模式
from abc import ABCMeta, abstractclassmethod

class Compiler(metaclass=ABCMeta):
    
    @abstractclassmethod
    def collectSource(self):
        pass

    @abstractclassmethod
    def compileToObject(self):
        pass

    @abstractclassmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):

    def collectSource(self):
        print("collection ios")

    def compileToObject(self):
        print("compile ios")

    def run(self):
        print("run elements")

class Client:

    def main(self):
        self.concreate = iOSCompiler()
        self.concreate.compileAndRun()


from abc import abstractclassmethod, ABCMeta

class Trip(metaclass=ABCMeta):

    @abstractclassmethod
    def setTransport(self):
        pass

    @abstractclassmethod
    def day1(self):
        pass
    
    @abstractclassmethod
    def day2(self):
        pass

    @abstractclassmethod
    def day3(self):
        pass
    
    @abstractclassmethod
    def returnHome(self):
        pass


    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()

class VeniceTrip(Trip):

    def setTransport(self):
        print("set Transport")

    def day1(self):
        print("transport day1")

    def day2(self):
        print("transport day2")

    def day3(self):
        print("transport day3")

    def returnHome(self):
        print("transport return home")

class MaldivesTrip(Trip):

    def setTransport(self):
        print("on foot, on any island, Wow")

    def day1(self):
        print("MaldivesTrip day1")

    def day2(self):
        print("MaldivesTrip day2")

    def day3(self):
        print("MaldivesTrip day3")

    def returnHome(self):
        print("MaldivesTrip return Home")

class TravelAgency(object):

    def arrange_trip(self):
        choice = input("input type: ")
        if choice == "historical":
            self.trip = VeniceTrip()
            self.trip.itinerary()
        
        elif choice == "beach":
            self.trip = MaldivesTrip()
            self.trip.itinerary()
    
if __name__ == "__main__":
    # hc1 = HealthCheck()
    # hc2 = HealthCheck()
    # hc1.add_server()
    # hc2.change_server()
    # print(hc1._servers)
    # temp = input("class name: ")
    # profile = eval(temp)()
    # print(profile.get_sections())
    # pizza = PizzaStory()
    # pizza.make_pizzas()
    # you = Your()
    # you.askEventManager()
    # test = Test()
    # del test
    # print(123)
    # you = You()
    # you.make_payment()
    # print(proxy_boss._get_current_object)
    # subject = Subject()
    # observer1 = Observer1(subject)
    # observer2 = Observer2(subject)
    # subject.notifyAll("notication")
    
    # news_publisher = NewPublisher()
    # for Subscriber in [SMSSubscriber, EmailSubscirber]:
    #     Subscriber(news_publisher)
    
    # news_publisher.add_news("hello world")
    # news_publisher.notifySubscribers()


    # print(news_publisher.subscribers())

    # news_publisher.add_news("hello world2")
    # news_publisher.notifySubscribers()

    # stock = StockTrade()
    # buy_stock = BuyStockOrder(stock)
    # sell_stock = SellStockOrder(stock)

    # # print(news_publisher.subscribers())

    # # news_publisher.add_news("hello world2")
    # # news_publisher.notifySubscribers()
    # print("开始运行")
    # http_server = tornado.httpserver.HTTPServer(RunApp())
    # http_server.listen(5000)
    # tornado.ioloop.IOLoop.instance().start()
    
    # agent = Agent()
    # agent.placeOrder(buy_stock)
    # agent.placeOrder(sell_stock)

    # context = Context()
    # stateB = ConcreteStateB()
    # stateA = ConcreteStateA()

    # context.setState(stateA)
    # context.Handler()

    # comp = Computer()
    # comp.change(On)
    # comp.change(Off)
    # comp.change(On)
    # # comp.change(Suspend)
    # # # comp.change(Hibernate)
    # comp.change(On)
    # comp.change(Off)
    
    # 运行
    # ios = iOSCompiler()
    # ios.compileAndRun()

    # client = Client()
    # client.main()

    TravelAgency().arrange_trip()

