"""
x = input('sayi 1 : ', )
y = input('sayi 2 : ', )

print(type(x and y))

toplam = int(x) + int(y)
print(toplam)

"""

x = 5               #int
y = 4.5             #float
name = "Caka Bey"   #str
isOnline = True     #bool

x = float(x)
print(x)
print(type(x))

y = int(y)
print(y)
print(type(y))

result = x+y
print(result)
print(type(result)) # cevap burda 9 olur cunku y int degerine donustu ve 4 degerini aldi. 

# bool to str

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline)) #bool ifadesi "True" olarak string oldu 


# bool to int

isOnline = True
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline)) #bool ifadesi 1 olarak integer oldu. False olsaydi cevap 0 olurdu.
