import random

#value = dir(random)
#value = help(random)
#print(value)

result = random.random()                        # 0.0 - 1.0
result = random.random() * 100                  # 0.0 - 100
result = int(random.uniform(10,100)) 
result = random.randint(1,100)

names = ['ali','veli', 'canan', 'hayriye','mustafa']
result = random.choice(names)                   # result = names[random.randint( 0, len(names)-1 )]

greating = 'hello there'
result   = random.choice(greating)              # if u use .choices intead of this -> output: 'l'



list_one = list(range(10))                      # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list_one)                        # Output: [3, 1, 4, 2, 6, 9, 5, 7, 8, 0]


list_one = range(100)
list_one = random.sample(list_one,3)            # Output: [8, 71, 34]
result  = random.sample(names,2)                # Output: ['canan', 'mustafa']



print(list_one)
print(result)  
