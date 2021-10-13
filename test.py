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

from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self):
        pass

class DeluxVeggiePizza(VegPizza):
    
    def prepare(self):
        print("prepare")

class ChickenPizza(NonVegPizza):

    def serve(self, VegPizza):
        print("serve", VegPizza)

class MexicanVegPizza(VegPizza):
    
    def prepare(self): 
        print("prepare")

class HamPizza(NonVegPizza):

    def serve(self, VegPizza):
        print("prepare", type(VegPizza).__name__)

class PizzaStory(object):
    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [USPizzaFactory()]:
            self.factory = factory
            self.NovVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NovVegPizza.serve(self.VegPizza)


if __name__ == "__main__":
    # hc1 = HealthCheck()
    # hc2 = HealthCheck()
    # hc1.add_server()
    # hc2.change_server()
    # print(hc1._servers)
    # temp = input("class name: ")
    # profile = eval(temp)()
    # print(profile.get_sections())
    pizza = PizzaStory()
    pizza.make_pizzas()

    
