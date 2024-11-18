x = 5 
y = 10 
z = 20

x, y ,z = 5,10,20

x, y = y, x

print(x,y,z)


x += 5              # x = x+5  
x -= 5              # x = x-5 
x *= 5              # x = x*5
x /= 5              # x = x/5

x %= 5              # x (mode 5)
x //= 5             # x'i 5'e boler ama kalan c degerini verir.

x **= 5             # x ust 5 => x^5

print(x,y,z)


values = 1,2,3      # veya => values = (1,2,3)

x, y, z = values

print(x, y, z)


values1 = 1,2,3,4,5,6
x, y, *z = values1  # *z ifadesi z bir listeye donusur. output = 1 2 [3, 4, 5, 6]
x, *y, z = values1  # output = 1 [2, 3, 4, 5] 6

print(x,y,z)
















