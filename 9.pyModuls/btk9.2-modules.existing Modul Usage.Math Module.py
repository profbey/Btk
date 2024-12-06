'''
******************** standart usage of modules ********************

import math

value = dir(math)
value = help(math)
value = help(math.factorial)
value = math.sqrt(49)
value = math.floor(5.9)
value = math.ceil(4.9)

print(value)



import math as islem                    # changed the math module here to "islem". 'math.function' -> updated to 'islem.function'
value = islem.factorial(5)


# yontem 2 

from math import *                      # Here we extracted everything from the math library. It's like moving a zip file to a folder.

value = sqrt(49)
print(value)

'''


from math import factorial,sqrt         # It only imports the functions that we will use.
