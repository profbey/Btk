# value types => str, number

x = 5 
y = 21

x = y     # x degeri artik y oldu. x degerine y degeri atanmis oldu.  

y = 10    # y ifadesine yeni deger atanmis oldu.

print(x,y)

# referance types => class, list


a = ['apple', 'banana']
b = ['apple', 'banana']

a = b               # esitlik kuruldugu icin referans adresleri eslesti. yapilan degisiklikler birbirine chain oldu. 


b[0] = 'grape'      # sifirinci index 'grape' il degistirildi. 

print(a,b)          # output: ['grape', 'banana'] ['grape', 'banana']
                    # output value type gibi degismek yerine b'de yapilan degisiklik dogrudan a'yi etkiledi.

