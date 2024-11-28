def square(num):                        # def square(num): return num **2
        return num **2

result = square(2)
print(result)



numbers = [1,3,5,7,9]

for i in map(square, numbers):          # it is the same thing as below without using list() method
        j = []
        j = j.append(i)
print(result)

result  = list(map(square,numbers))     # map(function, numbers) => for i in numbers: square(i)
print(result)

# if using a function once, lambda() expression can be use
result = list(map(lambda num: num **2,numbers))
print(result)


numbers = [1,3,6,7,12,42]

def checkEven(num):                     # checkEven = (lambda num: num %2 == 0)
        return num %2 == 0
result = list(filter(checkEven,numbers))
print(result)  

result = list(filter(lambda num: num %2 == 0, numbers))
print(result)
