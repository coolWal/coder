from functools import singledispatch

@singledispatch
def age(obj):
    pass

@age.register(int)
def _(a):
    print("我已经{}岁了".format(a))

@age.register(str)
def _(b):
    print("i am {} years old".format(b))

if __name__ == "__main__":
    age(12)
    age("hello")   
