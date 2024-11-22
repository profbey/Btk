for item in range(10):          # 0,1,2,3,4,5,6,7,8,9 
        print(item)             # There is ten numbers as index. 

for item in range(2,10):        # 2,3,4,5,6,7,8,9
        print(item)

for item in range(50,100,10):    # 50,60,70,80,90
        print(item)

print(list(range(50,100,10)))    # [50, 60, 70, 80, 90]
                                 # Starting from 50 and going up to 100 by 10s





# enumerate 'birer birer saymak'

index = 0 
greeting = 'hello world'

for letter in greeting:
        print(f"index: {index} letter: {letter}")       # or print(f"index: {index} letter:{greeting[index]})
        index +=1 



# alternative 'enumerate' method

greeting = 'hi there'

for indexN,letterN in enumerate(greeting):
        print(f'index: {indexN} letter: {letterN}')



# enumerate method // whats that?

method = 'enumerate'

for i in enumerate(method):
        print(i)



# zip method 

list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d','e','f']
list3 = [100,200,300,400,500,600]

print(list(zip(list1,list2)))                           # zipping by index numbers



for i1,i2,i3 in zip(list1,list2,list3):                 # alternative zipping
        print(i1,i2,i3)
