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


