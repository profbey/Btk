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

def usalma(a,b):
    start = time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish = time.time()
    totalTime = str(finish - start)
    print(f'function \'usalma\': {totalTime}')

def faktorial(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))
    finish = time.time()
    totalTime = str(finish - start)
    print(f'function \'faktorial\': {totalTime}')

usalma(5,6)
faktorial(13)
