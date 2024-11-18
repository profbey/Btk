x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1- Kullanicidan aldiginiz iki sayinin carpimi ile x,y,z toplaminin farki nedir

'''a = int(input("sayi ver #1: "))
b = int(input('sayi ver #2: '))

c = x+y+z

sonuc = (a * b) - c 

print(sonuc)'''

#2- y'nin x'e kalansiz bolumunu nedir

'''y = y //  x
print(y)'''

#3- (x,y,z) toplaminin mod 3"u nedir

toplam = (x+y+z) % 3
print(toplam)

#4- y ussu x'i hesaplayiniz

result = y **x 
print(result)
#5- x,*y,z = number islemine gore z'nin kupu nedir

numbers = (1,5,7,10,6)
(x,*y,z) = numbers
z = z**3
print(z)

#6- x,*y,z = number islemine gore y'nin degerleri toplami ne 

numbers = (1,5,7,10,6)
(x,*y,z) = numbers
a = len(y)
print(a)
toplam_y = y[a-1] +y[a-3] +y[a-2]  # daha otomatik yapmak icin for x in range(a) 
                                   # fonksiyonu ile yapacagiz muhtemelen.
































