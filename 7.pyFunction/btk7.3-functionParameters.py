def change(n):
        n[0] = 'istanbul'

cities = ['ankara', 'izmir']
 
change(cities)
print(cities)                           # Output = ['istanbul', 'izmir']



def add(a,b,c = 0):                     # c = 0 , if c is not given, 0 is taken as default. 
        return sum((a,b,c))             # This allows the function to work with 2 or 3 parameters.


print(add(10,30))



def add(*params):
        print(params)                   # it gives the value as a tuple.(*tuple)
        return sum(params)

print(add(10,20,30))                    # Regardless of the other,
print(add(10,20,30,40,50,60,70,70))     # the '*parameters' expression allows n assignments in this way.
                                        


def add(*params):
        summary = 0 
        for i in params:                # its the alternative of above function.
                summary = (summary + i)
        return summary



def userInfo(**args):                   # dic oldugunu belirtmek icin **args olarak girilir.(**dic)
        for key,value in args.items():
                print(f'{key} is {value}')
        print('*** ' * 10 + '\n')
     
userInfo(name= 'ahmet'  , age = 22, city = 'new york')
userInfo(name= 'mehmet' , age = 49, city = 'istanbul'   , phone = '+905445454545')
userInfo(name= 'cengiz' , age = 65, city = 'malatya'    , phone = '+905655454545', email = 'cengiz77@gmail.com')



def myFunction(a,b, *args, **kwargs):
        print(a)                        # Output = 10
        print(b)                        # Output = 20
        print(args)                     # Output = (30, 40, 50, 60)
        print(kwargs)                   # Output = {'key1': 'value 1', 'key2': 'value 2'}

myFunction(10,20,30,40,50,60, key1 = 'value 1', key2 = 'value 2') 
