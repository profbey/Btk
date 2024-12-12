fruit = {'orange','banana', 'apple', 'orange'}

# print(fruit[0]) -> indeklenemez.


for x in fruit:
     print(x)


fruit.add('cherry')
fruit.update(['mango', 'grape'])

fruit.remove('banana')
fruit.discard('apple')

fruit.pop()    #normalde indexlenebilir bir ifade olmus olsaydi sonuncuyu silerdi. indexlenemez oldugu icin random bir ifadeyi siler. 

print(fruit)

fruit.clear() # butun elemenlari siler.

print(fruit)





myList = [1,2,2,3,4,32,32,41,41,41,41,2,1]

a = set(myList)     # Tekrarlanan seyleri ortadan kaldirir listeyi tekillestirir.
a = sorted(a)       # siralama yapar. 

print(a) 
