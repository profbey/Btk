# 1- girilen bir sayinin 0-100 arasinda olup olmadigini kontrol edin 

try:
     x = float(input('Put A Number: '))
     
     if x<100 and x>0:
          print(f'The Number Is In Range')
     else:
          print(f'The Number ({x}) Is Out Of This Range')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')
     


# 2- girilen bir sayinin pozitif cift sayi olup olmadigini kontrol edin


try:
     x1 = float(input('Put A Number: '))
     
     if (x1 > 0) and (x1 %2 == 0):
          print(f'Sayi x1 ({x1}) is positive even number')
     elif (x1 > 0) and (x1 %2 != 0):
          print(f'Sayi x1 ({x1}) is positive odd number')
     else:
          print(f'Sayi x1 ({x1}) is out of range')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')


# 3- email ve parola bilgileri ile giris kontrolu yapin 

username = 'ahmetcvdr'   
password = 'a3253'

girilenUsername = input('Kullanici adi: ')
girilenPassword = input('Sifre: ')

if girilenPassword == password and girilenUsername == username:
     print('The Access is Approved')
else:
     print('The Access is Denied. Try Again!')


# 4- girilen 3 sayiyi buyukluk olarak karsilastirin

try:
     a = float(input('put the first number : '))
     b = float(input('put the second number : '))
     c = float(input('put the third number : '))
    
     
     if a>b>c:
          print(f'{a} > {b} > {c}')
     elif a>c>b:
          print(f'{a} > {c} > {b}')
     elif b>a>c:
          print(f'{b} > {a} > {c}')
     elif b>c>a:
          print(f'{b} > {c} > {a}')
     elif c>a>b:
          print(f'{c} > {a} > {b}')
     else:
          print(f'{c} > {b} > {a}')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')
     

# 5- kullanicidan 2 vize(60%) 1 final (40%) notuyla ortalama hesaplayin
#    a)Ortalama 50 olsa bile final notu en az 50 olmalidir.
#    b)Finalden 70 ve ustu alindiginda ortalamanin onemi olmasin

try:
     a = float(input('put the first number : '))
     b = float(input('put the second number : '))
     c = float(input('put the third number : '))
     
     avarage_midterm = (a * 0.3) + (b * 0.3)
     total_score =  avarage_midterm + (c * 0.4)

     if (c >= 70):
          print('You passed!\n Because you took 70+ score in final exam')
     elif (avarage_midterm >= 50 and c >= 50):
          print(f'You passed!\nThe total score in this course is {total_score}')
     else:
          print(f'You failed on this course with {total_score}')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')



# 6- kisinin vucut kitle endeksini hesaplayin 
#    (f : kilo / boy **2)
#    0    - 18.4 = zayif
#    18.4 - 24.9 = normal
#    25.0 - 29.9 = kilolu
#    29.9 - 34.9 = obez

user_name = input("What's your name? \n")

try:
     weight = float(input("Your Weight? : "))
     height = float(input("Your Height? : "))
     indexValue = (weight) / ((height/100) **2)

     if   0 <= indexValue and indexValue <= 18.4:
          print(f'{user_name} is weak with {indexValue}')
     
     elif 18.4 < indexValue and indexValue <= 24.9:
          print(f'{user_name} is normal with {indexValue}')
     
     elif 24.9 < indexValue and indexValue <= 29.9:
          print(f'{user_name} is fat with {indexValue}')
     
     else:
          print(f'{user_name} is obese with {indexValue}')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')


