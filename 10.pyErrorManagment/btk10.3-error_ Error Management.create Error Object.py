# Rasing an  Exception => password checking

'''

when a memory is received, the 'except' statement already gives us an error.

if we want to limit the function, we need to create our own error statement.
in this case, the 'raise Exception()' statement is used

'''

def check_password(psw):
       
        import re

        if len(psw) < 8:
                raise Exception('Password must be minimum 8 character.')
        elif len(psw) > 32:
                raise Exception('Password must be maximum 32 character.')
        elif not re.search('[a-z]', psw):
                raise Exception('Password must contain at least one lower case letter.')
        elif not re.search('[A-Z]', psw):
                raise Exception('Password must contain at least one upper case letter.')
        elif not re.search('[0-9]', psw):
                raise Exception('Password must contain at least one number.')
        elif not re.search('[_ @ # $ % &]', psw):
                raise Exception('Password must contain at least one alpha numeric character.')
        elif re.search(r'\s', psw):
                raise Exception('Password cannot contain space')
        else:
                print('The password is accepted.')


while True:
        try:
                password = input('Enter a valid password: ')
                check_password(password)
        except Exception as errorDisplay:
                print(errorDisplay)
        else:
                break