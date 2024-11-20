numbers = [6,46,33,34,54,7,78,9,49]

# 1- numbers listesini while ile ekrana yazdirin

'''i = 0 

while (i < len(numbers)):
        print(numbers[i])
        i += 1'''

# 2- baslangc ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari yazdirin 

'''
try:
        initialNumber = int(input('Entry first number: '))
        i = initialNumber
        finalNumber = int(input('Entry second number: '))
        j = finalNumber

        if i < finalNumber:
                while i < finalNumber:
                        i +=1 
                        if i % 2 == 1:
                                print(i)
                                                        
        elif j < initialNumber:
                while j < initialNumber:
                        j +=1
                        if j % 2 ==1:
                                print(j)
                                                        
        else:
                print('These numbers are equal each other')
        
except ValueError:
        print('Try again')


'''
# 3- 1 ile 100 arasindaki degerleri tersten yazdirin

i = 99 

while (i > 0):
        print(i)
        i -= 1


# 4- kullanicidan aldiginiz 5 sayiyi buyukten kucuge dogru yazdirin.

numbers = []

i = 0

while i<5:
        number = int(input('Enter a number: '))
        numbers.append(number)
        i += 1
numbers.sort()
print(numbers)


# 5- kullanicidan alacagiz n tane urun bilgisini liste icinde saklayin
#  **    urun sayisini kullaniciya sorun 
#  **   dic list yapisi (name, price) seklinde olsun 
#  **  urun ekleme islemi bittiginde whole ile listeleyin.





