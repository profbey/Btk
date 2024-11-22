# alternative of 'for' and 'while' methods 

numbers = []
for x in range(10):
        numbers.append(x)
print(numbers)

numbers = [x for x in range(10)]  # A for loop is created for the new x values (list) -- its an alternative to above scripts
print(numbers)



for i in range(10):
        print(i**2)

numbers = [x**2 for x in range(10)]



numbers = [x*x for x in range(10) if x%3 == 0 ]
print(numbers)




myString = 'hello'
myList   = []
for letter in myString:
        myList.append(letter)
print(myList)


myList = [letter for letter in myString]
print(myList)



years  = [1999,1997,2003,1966]
ages = [2019-year for year in years]
print(ages)




results = [ x if x%2 == 0 else 'odd' for x in range(10)]
print(results)



results = []
for x in range(3):
        for y in range(3):
                results.append((x,y))
print(results)               

numbers = [ (x,y) for x in range(3) for y in range(3)]
print(numbers)

numbers = [ (x,y,z) for x in range(3) for y in range(4) for z in range(5)]
print(numbers)
