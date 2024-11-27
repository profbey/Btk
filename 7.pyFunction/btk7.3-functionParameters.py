def change(n):
        n[0] = 'istanbul'

cities = ['ankara', 'izmir']
 
change(cities)
print(cities)                           # Output = ['istanbul', 'izmir']



def add(a,b,c = 0):                     # c = 0 , if c is not given, 0 is taken as default. 
        return sum((a,b,c))             # This allows the function to work with 2 or 3 parameters.


print(add(10,30))


def add(*params):
        print(params)                   # it gives the value as a tuple.
        return sum(params)

print(add(10,20,30))                    # Regardless of the other,
print(add(10,20,30,40,50,60,70,70))     # the '*parameters' expression allows n assignments in this way.
                                        









