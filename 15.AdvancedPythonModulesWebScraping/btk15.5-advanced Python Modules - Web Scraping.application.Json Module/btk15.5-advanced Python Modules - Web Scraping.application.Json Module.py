# farkli platformlarda veri aktarimi ve kullaniminda onemlidir.

import json

class User:
    def __init__(self,username,password,email,secim):
        self.username = username
        self.password = password
        self.email = email
        self.secim = secim


    pass

class UserRepository:
    def register(self):
        try:
     username =     input('Enter your ID: ').title()
     userAge  = int(input('How old are you?: '))
     userEdu  =     input("What is your education? ('elementary school', 'high school', 'university'): ").lower()
     levelEdu =     ['high school', 'university']

     if userAge >= 18:
          if userEdu in levelEdu:
               print(f'{username} can take a driver licence.')
          else:
               print(f'{username} cannot take a driver licence because of education level')
     else:
          print(f'{username} cannot take a driver licence because of age')

except ValueError:
     print('PLS ENTER AGAIN')


    def login(self):
        pass

    def saveToFile(self):
        pass

    def secilen(secim):
        



while True:
    print('Menu'.center(20,' '))

    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n \nYour Choice?: '.center(20,' '))

    if secim == '5':
        break
    else: 
        if secim == '1':
            #register
            pass
        elif secim == '2':
            #login
            pass
        elif secim == '3':
            #logout
            pass
        elif secim == '4':
            #identity
            pass
        else:
            False
