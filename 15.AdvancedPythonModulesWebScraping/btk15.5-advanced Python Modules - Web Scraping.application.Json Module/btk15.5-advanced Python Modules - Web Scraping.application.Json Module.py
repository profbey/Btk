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
        pass

    def login(self):
        pass

    def saveToFile(self):
        pass

    def secilen(secim):
        if secim == '5':
            exit()
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
        



while True:
    print('Menu'.center(20,' '))

    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n \nYour Choice?: '.center(20,' '))
    secilen(secim)