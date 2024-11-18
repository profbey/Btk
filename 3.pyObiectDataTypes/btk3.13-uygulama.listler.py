lst_ifade = 'bmw mercedes opel mazda subarru cupra'

#1- lst_ifade str'deki her ogeyi bir elemena cevir
lst_ifade = lst_ifade.split()
print(f'* listenin icindeki elemanlar : {lst_ifade}')

#2- liste kac elemanli
len_lst_ifade = len(lst_ifade)
print(f'\n* ex2 cevap : {len_lst_ifade}')

#3- listenin son ve ilk elemani ne
lst_ifade1 = lst_ifade[0] + ' ' + lst_ifade[-1]
lst_ifade1 = lst_ifade1.split()
print( f'\n* ex3 cevap : {lst_ifade1}')

#4- mazda degerini toyota ile degistirin 
lst_ifade[3] = 'toyota'
print(f'\n* yeni listenin icindeki elemanlar : {lst_ifade}')

#5- mercedes listenin bir elemani mi
result = 'mercedes' in lst_ifade
print(f'\n* in operatoru var/yok yanitina gore True/False degeri verir.\nCevap = {result}')


#6- listenin -2 index degeri ne 

result = lst_ifade[-2]
print(f'\n* ex6 cevap: {result}')

#7- listenin ilk 3 elemanini al 
print(f'\n* ex7 cevap: {lst_ifade[:3]}')


#8- listnein son iki elemani yerine "audi" ve "nissan" i al 
lst_ifade[-2:] = ['audi', 'nissan']
print(f'\n* ex8 lst icindeki elemanlar : {lst_ifade}')


#9- son elemani sil 
lst_ifade[-1] = []
lst_ifade.remove([])

#veya
del lst_ifade[-1] 
print(f'\n* ex9 lst icindeki elemanlar : {lst_ifade}')


#10- "renault" ifadesini ekle
lst_ifade.append("renault")
print(f'\n* ex10 lst icindeki elemanlar : {lst_ifade}')


#11- liste elemanlarini tersten yaz
lst_ifade = lst_ifade[::-1]
print(f'\n* ex11 lst icindeki elemanlar : {lst_ifade}')


#12- verileri bir liste halinde sakla.yeni liste elemanlarini ekrana yazdir

          #studentA: yigit bilgi   2010, (70,55,80)
          #studentB: bahadir sevgi 2005, (50,55,60)
          #studentA: ahmet arslan  2003, (46,56,89)



studentA = ['yigit' ,    'bilgi',      2010, [70,55,80]]
studentB = ['bahadir',   'sevgi',      2005, [50,55,60]]
studentC = ['ahmet' ,    'arslan',     2003, [46,56,89]]

studentKayit = []
studentList = [studentA,
               studentB,
               studentC]

for studentAppend in studentList :
     studentKayit.append(studentList)
exit
     
print(f'\n* ex12 StudentKayit icindeki elemanlar : {studentKayit}')
  