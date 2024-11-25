"""
Daire Alani : nr^2
Daire Cevresi : 2nr

Yari capi verilen dairenin alani ve cevresini hesaplayiniz. (n = 3.14)

"""
pi = 3.14
r = input("radius: ")
r = float(r)

area = pi * (r ** 2)
surrounding = 2 * pi * r 

print(f'Circle Area: {area}, \nCircumference of Circle: {surrounding}')
print('*** ' *10)



