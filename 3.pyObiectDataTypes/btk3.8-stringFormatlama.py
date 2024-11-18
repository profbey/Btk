name = "Aly Ata"
surname = "BAK"

print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname)) #siralamayi degistirir. Hint: index numarasi saymaya sifirdan baslar.
print("My name is {n} {s}".format(n=name,s=surname))

age = 31
print("My name is {} {} and i am {} years old.".format(name,surname,age))

result = 1200/ 700
print('the result is {r:1.4}'.format(r=result)) # 1 ifadesi noktadan once kac basamak gozukecek,
                                                # 4 kismi ise vurgulden sonra kac basamak gosterecegini soyler.


# f-string 

print(f"My name is {name} {surname} and i am {age} years old.") 

# formatlama ile ayni sey sadece .format(name) yerine {name} icerisine dogrudan yazabiliriz.



