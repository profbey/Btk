"""
Daire Alani : nr^2
Daire Cevresi : 2nr

Yari capi verilen dairenin alani ve cevresini hesaplayiniz. (n = 3.14)

"""
pi = 3.14
r = input("yaricap: ")
r = float(r)

alan = pi * (r ** 2)
cevre = 2 * pi * r 

print(f'Ucgenin Alani: {alan}, \nUcgenin Cevresi: {cevre}')
print('*** ' *10)




"""
Sadece kenarlari bilinen ucgenin alani hesaplama yontemi >> 

a, b ve c ucgenin kenar uzunluklari ve s 
ucgenin cevre uzunluğunun yarisi olmak uzere;

Alan = √(s(s-a)(s-b)(s-c)) formuluyle hesaplanir.

"""

print('Method for calculating the area of ​​a triangle with only known sides')

from math import sqrt

while True:
        try:
                a = float(input("birinci kenar: "))
                b = float(input("ikinci kenar: "))
                c = float(input("ucuncu kenar: "))

                if (a < b+c) and (b < a+c) and (c < b+a):

                        s = (a + b + c) * 0.5 
                        alan_ucgen = sqrt(s * (s-a) * (s-b) * (s-c))
                        alan_ucgen = float(alan_ucgen)

                        print(alan_ucgen)

                        break
        except ValueError:
                print('It is not a triangle. Try again!')
print('*** ' *10)
        