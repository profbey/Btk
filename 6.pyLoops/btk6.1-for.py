numbers = [1,2,3,4,5,6,7]

for prtNum in numbers: 
        print(prtNum)



ID = ['mustafa', 'murat', 'mete']

for names in ID:
        print(names)



tuple_ex = [(1,2),(2,4),(3,6),(5,3)]

for a,b in tuple_ex:
        print(a)
        print(a,b)




students = {
     '120' : {
          'name'    : 'mete',
          'surname' : 'uzum',
          'phone'   : '54545447756'
     },
     '121': {
          'name'    : 'ahmet',
          'surname' : 'gozupek',
          'phone'   : '53453663142'
     },
     '122': {
          'name'    : 'unali',
          'surname' : 'turan',
          'phone'   : '53256461212'
     }
} 

for firstVal,secondVal in students.items():             # Eleman gruplarina ulasmak icin .item() cagirilmali
        print(secondVal)


 