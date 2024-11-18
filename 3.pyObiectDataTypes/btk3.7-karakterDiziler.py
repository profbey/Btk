name = "Kilimcinin"
surname = "Koroglu"
age = 31 

greating = f"My name is {name} {surname} and, \nI am {age} years old" # f" {} " ifadesi str ifadeye inject edebilmemize yardimci olur. 
print(greating)                                                       # \n ifadesi ise satiri asagiya atar.
print(greating.capitalize(58))

print(greating[0])
print(greating[1])          # bosluk dahil her karakter bir indexleme islemi vardir. ifadeler sayilmaya 0'dan baslanir.
print(greating[2])
print(greating[3])

length = len(greating)      # bu greating fonksiyonunda toplam kac karakter var onu gosterir.
print(greating[length - 1]) # sifirdan basladigi icin, karakter sayisi -1 son karakteri verecektir.
print(greating[-1])         # ya da bu ifade dogrudan geriye saydigi icin son karakteri verecektir.

print(greating[3:7])        # dorduncu karakterden yedinci karaktere kadar yazdirir. 
print(greating[3: ])        # dorduncu karakterden sonuna kadar yazdirir.
print(greating[ :8])        # en bastan dokuzuncu karaktere kadar yazdirir.
print(greating[2:40:2])     # ucuncu karakterden kirkbirinci karaktere kadar iki karakterde bir alir.






