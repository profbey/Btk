# Examples: Find whether an entered number is prime or not.

    

print('This app checks if the number is prime or not')
from math import sqrt

try:
    number = int(input('Enter a number: '))
    numberSqrt = int(sqrt(number))
    primeNumber = True

    for i in range(2, numberSqrt + 1):
        if number % i == 0:
            primeNumber = False
            break
        
except ValueError:
    print('try again with numbers.')


if primeNumber:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is NOT prime.")




