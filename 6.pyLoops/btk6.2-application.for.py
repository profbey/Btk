numbers = [6,46,33,34,54,67,78,98,49]

# 1- Numbers listesindeki hangi sayilar 3'un katidir? 

for num3 in numbers:
        if (num3 %3 == 0):
                print(num3) 

# 2- Numbers listesindeki sayilarin toplami kactir?

total = 0

for numT in numbers:
        total = total + numT
print('Total = ',total)

# 3- Numbers listesindeki tek sayilarin karesini liste olarak yazdir.

for sq in numbers:
        if (sq %2 == 1):
                print(sq **2)

# 4- Cities  listesindekilerin hangileri en fazla 5 karakterlidir?

cities = ['istanbul', 'ankara', 'izmir', 'bursa', 'kahramanmaras', 'kocaeli', 'nigde']

for cty in cities:
        if (len(cty) <= 5 ):
                print(cty)



# 5- Products listesindeki tum urunlerin fiyatlari toplami nedir?
products = [
        {'name' : 'samsung s15' , 'price' : '3000' },
        {'name' : 'samsung s16' , 'price' : '4000' },
        {'name' : 'samsung s17' , 'price' : '5000' },
        {'name' : 'samsung s18' , 'price' : '6000' },
        {'name' : 'samsung s19' , 'price' : '7000' },
        {'name' : 'samsung s20' , 'price' : '8000' },
        {'name' : 'samsung s21' , 'price' : '9000' }
]

sum = 0
for prd in products: 
        prc = int(prd['price'])
        sum = sum + prc
print(sum)


# 6- Products listesindeki urunlerden fiyati en fazla 6000 olan urunleri yazdiriniz.

for prd in products:
        prc = int(prd['price'])
        if prc <= 6000:
                print(prd['name'])
  