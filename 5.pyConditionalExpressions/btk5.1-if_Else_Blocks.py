'''isLoggedin = True

if isLoggedin:
     print('isloggedin fonksiyonu True oldugu icin calisir')

'''


username = 'ahmetcavdar'   
password = 'a3253'

girilenUsername = input('Kullanici adi: ')
girilenPassword = input('Sifre: ')

if girilenUsername == username:
     if girilenPassword == password:
          print('The Access is Approved')
     else:
          print('The Access is Denied. Password is Incorrect!')   
else:
     print("The Access is Denied. The User Couldn't Be Found!")

