#1- girilen 2 sayidan hangisi buyuktur?

try:
     sayi1 = int(input('sayi1 gir: '))
     sayi2 = int(input('sayi2 gir: '))

     if sayi1 > sayi2:
          print(f'sayi1: {sayi1} > sayi2: {sayi2}')
     elif sayi1 == sayi2:
          print(f'sayi1: {sayi1} = sayi2: {sayi2}')
     else:
          print(f'sayi1: {sayi1} < sayi2: {sayi2}')

except ValueError:
     print("try again") 
     print("*** " * 5)



#2- kullanicidan 2 vize(60%) ve final(40%) notunu alip ortalama hesaplayin 
#   eger ortalama 50 ve uzeriyse 'gecti', kaldiysa 'kaldi' yazdirin.

vize1 = input('Entry first midterm score: '.title())
vize2 = input('Entry second midterm score: '.title())
final = input('Entry final score: ')

try :
     totalPuan = (float(vize1) * 0.3) + (float(vize2) * 0.3) + (float(final) * 0.4)
     if totalPuan >= 50:
          print(f'student passed this course {totalPuan}'.title())

     else:
          print(f'Unlucky bro. you failed this course {totalPuan}'.title())

except ValueError: 
     print('try again. your input should be integer.'.upper())


      

#3- girilen bir sayinin tek mi cift mi oldugunu yazdirin. 

try :
     sayi = int(input('Sayi Girin: '))

     if (sayi % 2 == 0):
         print(f'Girilen Sayi CIFT SAYI ')
     else:
          print(f'Girilen Sayi TEK SAYI ')
except ValueError:
     print('the input is not appropriate, try again !!!'.upper())
print('*** ' * 5)





#4- girilen sayinin negatif pozitif durumunu yazdirin 

try :
     sayi = int(input('Sayi Girin: '))

     if (sayi > 0 ):
         print(f'Girilen Sayi POZITIF SAYI ')
     elif (sayi == 0 ):
         print(f'Girilen Sayi SIFIR ')
     else:
          print(f'Girilen Sayi NEGATIF SAYI ')

except ValueError:
     print('the input is not appropriate, try again !!!'.upper())
print('*** ' * 5)
     




#5- parola ve email bilgisini isteyip dogrulugunu kontrol edin. 
#   username = 'ahmetcavdar'   password = '3253'


username = 'ahmetcavcav'   
password = 'a3253'

girilenUsername = input('Kullanici adi: ')
girilenPassword = input('Sifre: ')

if girilenPassword == password and girilenUsername == username:
     print('The Access is Approved')
else:
     print('The Access is Denied. Try Again!')





