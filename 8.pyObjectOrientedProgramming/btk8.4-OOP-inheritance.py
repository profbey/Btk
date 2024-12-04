# Inheritance (kalitim) : miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher  


# Animal => Dog(Animal), Cat(Animal)


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person was created.')

class Student(Person):
    def __init__(self, fname, lname):                   # Add fname and lname as arguments
                                                # Use super() to call the parent class's __init__ method.
                                                # This automatically handles the 'self' argument correctly.
        super().__init__(fname, lname)                  # Pass only fname and lname to super().__init__
        print('Student was created.')

p1 = Person( 'murat'  , 'cinar')
s1 = Student('mehmet' , 'yilmaz')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)




 