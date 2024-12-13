'''
def my_decorater(func):
    def wrapper():
        print('before function')
        func()
        print('after function')
    return wrapper

def sayHello():
    print('hello')

def sayGreating():
    print('greating')

sayHello = my_decorater(sayHello)
sayHello()

sayGreating = my_decorater(sayGreating)
sayGreating()
'''



def my_decorater(func):
    def wrapper(name):
        print('before function')
        func(name)
        print('after function')
    return wrapper

@my_decorater
def sayHello(name):
    print(f'hello {name}')

sayHello('user')



import math
import time

def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish = time.time()
        totalTime = str(finish - start)
        
        print(f'function {func.__name__}: {totalTime}')
    return inner

@cal_time
def usalma(a,b):
    print(math.pow(a,b))

@cal_time
def faktorial(num):
    print(math.factorial(num))

usalma(5,6)
faktorial(13)



