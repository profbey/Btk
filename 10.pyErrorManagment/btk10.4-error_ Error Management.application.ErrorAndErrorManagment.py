# Find the numeric values ​​in the list elements.

lst = ['7','3','5a','10b','abc']

for x in lst:
        try:
                result = int(x)
                print(result)
        except ValueError:
                continue



# Make sure that every input you get is a number unless the user enters a 'q' value

while True:
        nmb = input('number: ')
        if nmb == 'q':
                break
        
        try:
                result = float(nmb)
                print(f'Valid entery: {result}')
                break
        except Exception:
                continue



# The entered password gives a Turkish character error in ocomde

def checkPassword(psw):
        tr_characters = 'ğüşiçöşıİĞÜŞÇÖ'
        for i in psw:
                if i in tr_characters:
                        raise TypeError('Password cannot include turkish character')
                else:
                        pass
        print('Valid password')
                
psw = input('password: ')

try:
        checkPassword(psw)
except TypeError as error:
        print(f'ERROR: {error}')



# Creates the factorial function and displays error messages for the value that comes to the function.

def factorial(x):
        x = int(x)

        if x < 0:
                raise ValueError('Negative Value')

        result = 1 
        
        for i in range(1,x+1):
                result *= i

        return result         

for x in [6,11,22,'10b',-8]:
        try:
                y = factorial(x)
        except Exception:
                continue

        print(y)
