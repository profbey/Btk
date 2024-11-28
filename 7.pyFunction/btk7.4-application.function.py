# Gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyon yazin.


def display(name,n):
        '''
        DOCSTR: Write a function that displays a sent word 
                on the screen for a specified number of times.

        INPUT : display(name,n)
        OUTPUT: name * n
        '''
        while n > 0:
                print(name)
                n -= 1 
        
try: 
        name = input('whats your name?: ')
        n    = int(input('how many time you want to screen?: '))
        display(name,n)

except ValueError:
        print('try again')


 
# Kendine gonderilen sinirsiz sayidaki parametreyi bir listeye ceviren bir fonksiyon yazin.


def add(*params):
        myList = []

        for i in range(params):
                myList.append(i)
        return myList


# Gonderilen 2 sayi arasindaki tum asal sayilari bulun. 


# Kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde dondurun.

def find_intDivisor(userNumb):
    '''
        DOCSTR: Fills in a list of the integers of a number sent to it.

        INPUT : find_intDivisor(userNumb)
        OUTPUT: intDivisor = [values]
    '''   
    
    intDivisor = []

    if userNumb > 0:                                          
        for number in range(1, userNumb + 1):       # Iterate through numbers from 1 to userNumb (inclusive)
                                                
                if userNumb % number == 0:              # Check if userNumb is divisible by the current number
                        intDivisor.append(number)           # If divisible, add to the list
        return intDivisor
    
    elif userNumb == 0:
           print('it is equal to zero.')

    else:
           print('it is negative number.')

try:
    userKey  = int(input('enter a number: '))
    result = find_intDivisor(userKey) 
    print(result) 

except ValueError:
    print('try with numbers')














