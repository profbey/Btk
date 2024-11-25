'''
1 - 100 arasinda rastgele uretebilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin.

** 'random' modulu icin 'python random' seklinde arama yapin.
** 100 uzerinden puanlama yapin. her soru 20 puan.
** hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.


***** 
'''
import random

randomNumber = random.randint(1, 10)

try:                                            # Its for input of right.
    health = int(input('How many right you want?: '))
    right = health
except ValueError:
    right = 5 
print(f"You have {right} right.")

counter = 0 
score = 100

while right > 0:
    try:
        
        estimate = int(input('Your Estimate : '))
        right -= 1

        if randomNumber == estimate:
            print(f'Congratulations, You got it right the {counter + 1 }. time.\nYour score is {score} ')
            break
        elif randomNumber > estimate:
            print('up')
        else:
            print('down')

        
        if randomNumber != estimate:            # Deduct points only for incorrect guesses
            counter += 1
            score -= (100/health) * counter 

        if right == 0:
            print(f'You LOSE. The Number is {randomNumber}')
            break
        
    except ValueError:
        print('Try again with numbers!')

