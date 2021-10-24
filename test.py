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

# 简单工厂模式
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

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")
    
class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublictionSection(Section):
    def describe(self):
        print("publiction Section")

class Profile(object):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections
    
    def add_sections(self, section):
        self.sections.append(section)
    
class Linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection)
        self.add_sections(PatentSection)
        self.add_sections(PublictionSection)

class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection)
        self.add_sections(AlbumSection)

if __name__ == "__main__":
    # hc1 = HealthCheck()
    # hc2 = HealthCheck()
    # hc1.add_server()
    # hc2.change_server()
    # print(hc1._servers)
    temp = input("class name: ")
    profile = eval(temp)()
    print(profile.get_sections())


    
