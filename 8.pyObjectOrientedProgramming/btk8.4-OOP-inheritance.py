# Inheritance (kalitim) : miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher  


# Animal => Dog(Animal), Cat(Animal)




class Person():

    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        
    def whoAmI(self):
        print(f'I am {self.firstName} {self.lastName}')
    
    def rangeAttack(self):
        print(f'I HAVE 14M FOLLOWERS ON INSTAGRAM')
    


class Student(Person):
    def __init__(self, fname, lname, number):                   # Add fname and lname as arguments
                                                # Use super() to call the parent class's __init__ method.
                                                # This automatically handles the 'self' argument correctly.
        super().__init__(fname, lname)                  # Pass only fname and lname to super().__init__
        self.phoneNumber = number

    def sayHi(self):
        print(f'Hey {self.name}')

    def rangeAttack(self):                      # Override to rangeAttack of Person() class  
        print(f"I'VE COACHED THE BEST CLUBS IN THE WORLD")

p1 = Person('Ibrahim', 'Yilmaz')
s1 = Student('Jose'  , 'Morinho', 1441512)

#print(p1.firstName + ' ' + p1.lastName)
#print(s1.firstName + ' ' + s1.lastName + ' ' +  )

#p1.whoAmI()
#p1.rangeAttack()

s1.whoAmI()
s1.rangeAttack()
 