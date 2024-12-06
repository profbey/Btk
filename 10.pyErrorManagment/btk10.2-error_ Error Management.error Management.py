'''
# Error Handling 


x = input('Enter x value: ')
y = input('Enter y value: ')
print(x / y)                                                    # when entering y = 0 or str value, valueError or zeroValueError can be occurred



try:
        x = float(input('Enter x value: '))
        y = float(input('Enter y value: '))
        print(int(x / y))
except ZeroDivisionError :                                      # or 'except ZeroDivisionError,ValueError:'
        print('y value cannot be zero')
except ValueError:
        print('x and y should be integer')

        

try:
        a = float(input('Enter a value: '))
        b = float(input('Enter b value: '))
        print(int(a / b))
except (ZeroDivisionError,ValueError) as errorDisplay:                     
        print('Wrong entry, pls use valid value')
        print(errorDisplay)


try:
        i = float(input('Enter i value: '))
        j = float(input('Enter j value: '))
        print(int(i / j))
except:                                                         # It can be used if the type of error is not important, but we cannot see the type of error this way.
        print('Wrong entry, pls use valid value')

        
              
try:
        val1 = float(input('Enter val1 value: '))
        val2 = float(input('Enter val2 value: '))
        print(int( val1 /val2 ))
except:                                                
        print('Wrong entry, pls use valid value')
else:
        print('everything is okey')                             # else of except. so, this try is working and print('everything is okey')    
'''

def value():
        while True:
                '''
                The function goes into a loop until the try part is executed.
                When the value of type is reached, the else part stops.
                '''      
                try:
                        val1 = float(input('Enter val1 value: '))
                        val2 = float(input('Enter val2 value: '))
                        print(int(val1 /val2))
                except Exception as errorDisplay:                                                
                        print(f'Wrong entry: "{errorDisplay}", pls use only valid value!')
                else:
                        break
                finally:
                        print("'Value()' funtion ended.")       # This part is executed regardless of the operation in each round.                

value()                                                         # To start the defination.
