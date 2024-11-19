numbers = [6,46,33,34,54,7,78,9,49]

# 1- numbers listesini while ile ekrana yazdirin

i = 0 

while (i < len(numbers)):
        print(numbers[i])
        i += 1

# 2- baslangc ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari yazdirin 

numbers = [6,46,33,34,54,7,78,9,49]


try:
        initialNumber = int(input('entry first number: '))
        i = initialNumber
        finalNumber = int(input('entry second number: '))
        j = finalNumber

        if finalNumber < numbers and numbers < initialNumber:
                while j < i:
                        j = j +1
                        print(j)
                
        elif initialNumber < numbers and numbers < finalNumber :
                while i < j:
                        i = i +1
                        print(i)
        

except ValueError:
        print('try again')



# 3- 1 ile 100 arasindaki degerleri tersten yazdirin

# 4- kullanicidan aldiginiz 5 sayiyi buyukten kucuge dogru yazdirin

# 5- kullanicidan alacagiz n tane urun bilgisini liste icinde saklayin
#  **    urun sayisini kullaniciya sorun 
#  **   dic list yapisi (name, price) seklinde olsun 
#  **  urun ekleme islemi bittiginde whole ile listeleyin.





