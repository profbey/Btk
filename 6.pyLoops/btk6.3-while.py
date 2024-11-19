x = 1           # numbers = btw 1-100

while (x < 100) :
        if (x %2 == 0 ):
                print('only even numbers in range:',x)
        else:
                print('only odd numbers in range:',x)
        x += 1


name = ''       # False

while not name.strip():
        name = input('Name?: ')
print(f'Wellcome, {name.title()}.')

# 'while True:' seklinde calisir.
        