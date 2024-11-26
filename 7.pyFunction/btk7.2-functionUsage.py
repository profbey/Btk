# function 

def sayHello():                                            # to define a function to remind all calculations
        print('hello')               



def sayHello_v2(username):
        print(f'Wellcome {username}')

username = 'osman' 
sayHello_v2('osman')
sayHello_v2(username)

username2  = input('Say your2 name!: ')
sayHello_v2(username2)



def sayHello_v3(username = 'mustafa'):                  # if any parameters didn't say, except to 'mustafa' 
        return 'Wellcome ' + username                   # return - return the value back. sayHello = 'Wellcome ' + 'mustafa' 

msg = sayHello_v3()
print(msg)

username3  = input('Say your3 name!: ')                 # return sayHello = 'Wellcome ' + input value
msg3 = sayHello_v3(username3)
print(msg3)



def total(num1, num2):
        return num1 + num2

int1 = int(input('in1: '))
int2 = int(input('in2: '))
result = total(int1, int2)
print(result)



def ageCalculater(YearOfBirth):                 # Finding UserAge

        """This calculate your birth 
        ageCalculater = Now - Year of Birth"""

        import datetime
        nowYear = datetime.datetime.now().year

        return nowYear - YearOfBirth


def whenRetirement(userYear):                   # Finding how many year left to retirement by using UserAge  
        '''
        DOCSTR: Finding how many year left to 
        retirement by using ageCalculater function.

        INPUT : Year Of Birth
        OUTPUT: Calculated year information
        '''                        
        age = ageCalculater(userYear)
        retirement = 65 - age

        if retirement > 0:
                print(f'{retirement} years left until retirement.')
        else:
                print(f'You have already retired.')



userYear = int(input('when did you birth?(year): '))
age     = ageCalculater(userYear)
whenRetirement(userYear)

print(f'You are {age} years old')
print('*** ' * 10 + '\n')

print(help(whenRetirement))                     # help() - defines the function by docstring