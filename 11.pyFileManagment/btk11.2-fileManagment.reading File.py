try:
          file = open('C:/Users/User/Desktop/newFile2.txt','r',encoding='utf-8')
except FileNotFoundError:
        print('the file doesnt exist')
finally:
          file.close()
        
# there are many method to read file

# For Loop                              -> print fonksiyonu isini bitirdikten sonra bir satir boslugu birakir
for i in file:
        print(i,end= "")                ## bosluk birakmasin diye bu sekilde komut girebiliriz.
file.close

# read() function                       -> Print fonsiyonundaki gibi satir arasi boslugu birakmaz
content = file.read()
print(content)
file.close


content1 = file.read()
print(' content 1 '.center('*',30))
print(content1)

content2 =file.read()                   # open() fonsiyonu imleci biraktigi yerden acar.
print(' content 2 '.center('-',30))     # bu yuzden, content2 dosyasi bos olur. print() bir sey yazamaz.
print(content2)                         # print() bir sey yazamaz.
file.close



contentFile = file.read(5)              # ilk 5 karakteri yazdirir.
contentFile = file.read(3)              # codu tekrar calistirdigimizda sonraki 3 karakteri yazdirir.
contentFile = file.read(3)              # codu tekrar calistirdigimizda sonraki 4 karakteri yazdirir.

print(contentFile)
file.close



# readline() function                   -> her okuma islemini satir olarak yapar ama sona bir satir boslugu birakir.

print(file.readline(),end='')                  #  ilk satiri yazdirir
print(file.readline(),end='')                  #  ikinci satiri yazdirir
print(file.readline(),end='')                  #  ucuncu satiri yazdirir

file.close


# readlines() function                  -> her satiri alip bir liste elemani olarak yazdirir.Ancak, her elemanin sonuna \n ekler.

lst = file.readlines()

print(lst)

file.close
