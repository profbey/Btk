################################# ENCAPSULATION #################################
'''
def outer(num1):
    def inner_increment(num1):
        return num1 + 1 
    
outer(10)           # icteki fonksiyonu calistirmaz. 10 degeri bosa duser.


def outer(numb1):
    print('outer func,not inner increment')
    def inner_increment1(numb1):
        return numb1 + 1 
    numb2 = inner_increment1(numb1)
    print(numb1, numb2)

outer(10)           # icteki fonksiyonu cekmek icin icine yazdik. yani bu bir kapsulleme islemidir.
#*** bu islem karmasik fonsiyonlarda,programlarda optimizasyon ve calismanin basitlestirmesi icin onemlidir.
'''

def factorial(number):

    if not isinstance(number, int):
        raise TypeError('number must be a integer')
    if not number >= 0:
        raise ValueError('number must be positive number')
 
    def inner_factorial(number):
        if number <=1:
            return 1 
        return number * inner_factorial(number -1)
    return inner_factorial(number)

try:
    print(factorial(5))
except Exception as ex:
    print(f'{ex}: the value must be x>0 and integer')
