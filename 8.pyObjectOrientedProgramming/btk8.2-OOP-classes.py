# class
class Person:
        pass

        # class attributes
        address = 'no info'

        # constructor (yapici methods)
        def __init__(self, name, year ):                        # The first index is self as stock. it is changeable
               

                # object attributes
                self.name = name
                self.year = year
                print('The init method is working **CheckPoint')

                # methods  
                


# object (instance)
p1 = Person('mustafa', 1990)
p2 = Person(name = 'ramazan', year = 1996)

# updates
p1.name = 'ahmet'
p1.address = 'Birmingham, UK'

# accessing object attributes
print(f'name: {p1.name}, birthday date: {p1.year} and address info: {p1.address}')
print(f'name: {p2.name}, birthday date: {p2.year} and address info: {p2.address}')
