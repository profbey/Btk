# Example 1 

name = 'mustafa kucuk'

for letter in name:

        if letter == 'f':
                break           
        
        print(letter)           # Output : m u s t a 



# Example 2

x = 0 

while x < 5:
        x += 1  
        if x == 2:              # Output : 1 3 4 5 (no '2')
                continue
        print(x)
                        
 # Example 3 : What is the sum of positive numbers up to 100?

x = 0 
result = 0

while x <= 100 :
        x += 1 
        if x % 2 == 1:          # to pass odd numbers
                continue
        result += x 
        
print(f'Total : {result}')
