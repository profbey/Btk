'''
1 - 100 arasinda rastgele uretebilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin.

** 'random' modulu icin 'python random' seklinde arama yapin.
** 100 uzerinden puanlama yapin. her soru 20 puan.
** hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.

'''

import random

sayi = random.randint(1,50)
hak = 5
sayac = 0

while hak <= 5:
        try:

                tahmin = int(input('assumption : '))
                hak -= 1
                sayac +=1
        

                if sayi == tahmin:
                        print('congrat')
                        break
                elif sayi > tahmin:
                        print('up')
                else:
                        print('down')


                if hak == 0 :
                        print(f'you lose. the assumption number is {sayi}')
                        break
        except ValueError:
                print('try again with numbers')



