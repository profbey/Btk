
# 1- Kullanicidan isim, soyisim, yas, egitim bilgisi alinacak.   
#    Kosullar: 18+ yas egitim durumu lise veya universite mezunu olmali

try:
     userName =     input('Enter your ID: ').title()
     userAge  = int(input('How old are you?: '))
     userEdu  =     input("What is your education? ('elementary school', 'high school', 'university'): ").lower()
     levelEdu =     ['high school', 'university']

     if userAge >= 18:
          if userEdu in levelEdu:
               print(f'{userName} can take a driver licence.')
          else:
               print(f'{userName} cannot take a driver licence because of education level')
     else:
          print(f'{userName} cannot take a driver licence because of age')

except ValueError:
     print('PLS ENTER AGAIN')






# 2- Bir ogrenciden 2 sozlu notu istenip not araligina karisilik gelen not bilgisini yazin.
#    0 <= x <= 24  = 0 
#    24 < x <= 44  = 1
#    44 < x <= 54  = 2
#    54 < x <= 69  = 3 
#    70 < x <= 84  = 4
#    84 < x <= 100 = 5

while True:
     try:
          sozluFist   = float(input('Entry your first oral examination: '))
          sozluSecond = float(input('Entry your second oral examination: '))
          x = (sozluFist + sozluSecond) / 2 

          if 0 <= x <= 24:
               print(f'Your grade is 0 with {x} score.')
          elif 24 < x <= 44:
               print(f'Your grade is 1 with {x} score.')
          elif 44 < x <= 54:
               print(f'Your grade is 2 with {x} score.')
          elif 54 < x <= 69:
               print(f'Your grade is 3 with {x} score.')
          elif 70 < x <= 84:
               print(f'Your grade is 4 with {x} score.')
          elif 84 < x <= 100:
               print(f'Your grade is 5 with {x} score.')
          else:
               print(f'Your grade is out of with {x} score.')    # if it is negative
          break
     except ValueError:
          print('Enter your data again!')
     




# 3- Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesaplayiniz.
#    1. bakim = 1. yil  
#    2. bakim = 2. yil 
#    3. bakim = 3. yil 
#    ** Sure hesabini alinan gun, ay, yil bilgisine gire gun bazli hesaplayiniz.
#    *** datetime modulunu kullanmaniz gerekiyor.
#    (simdi) - (2022/3/2) = gun

import datetime
 
while True:
     try:
          date = input("What's The Date Of The Vehicle Been In Traffic? (2022/3/2) :")
          date = date.split('/')

          trafficTime = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
          timeNow = datetime.datetime.now()

          difTime = (timeNow - trafficTime)
          difTime.days
          
          if   0         <= difTime.days <= 365:
               print(f'It is on the first maintenance year with {difTime.days} days.')
          elif 365       <  difTime.days <= (365 *2):
               print(f'It is on the second maintenance year with {difTime.days} days.')
          elif (365 *2)  <  difTime.days <= (365 *3):
               print(f'It is on the third maintenance year with {difTime.days} days.')
          else:
               print(f'It is on the fourth maintenance term with {difTime.days} days.')
          break
     
     except ValueError:
          print('Pls entry available numbers')

