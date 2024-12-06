# error

# error handling -> Error managment

'''
A piece of information was requested from the user, but;
the user entered a data that should be given as int in str format
the program gives an error at this point and stops working
it is necessary to prepare for the errors that we may receive before the error occurs.

for example:

print(a)                -> NameError    // 'not defined' error
b = int('1a3')          -> value error // it cannot be changed as integer because of 'a'
print(10/0)             -> ZeroDivisionError
print('hell'o)          -> SyntaxError: invalid syntax

instead of catching all of these one by one, we should evaluate them under the error heading.

https://docs.python.org/3/library/exceptions.html => Exceptional hierarcy

'''










