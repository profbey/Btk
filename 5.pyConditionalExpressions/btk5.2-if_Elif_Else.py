
user_name = input("What's your name? \n")

try:
     weight = float(input("Your Weight? : "))
     height = float(input("Your Height? : "))
     indexValue = (weight) / ((height/100) **2)

     if   0    <= indexValue  <= 18.4:
          print(f'{user_name} is weak with {indexValue}')
     
     elif 18.4 < indexValue   <= 24.9:
          print(f'{user_name} is normal with {indexValue}')
     
     elif 24.9 < indexValue   <= 29.9:
          print(f'{user_name} is fat with {indexValue}')
     
     else:
          print(f'{user_name} is obese with {indexValue}')

except ValueError:
     print('TRY AGAIN WITH A NUMBER')


























