class Circle:
        # Class object attributes
        pi = 3.14159265359

        def __init__(self, radius = 1):
                self.radius = radius

        # methods
        def surrounding(self):
                return 2 * self.pi * self.radius
                

        def area(self):
                return  self.pi * (self.radius ** 2)
               
                

c1 = Circle()   # r = 1
c2 = Circle(3)  

print(f'circle1 area is {c1.area()}, circle surrounding is {c1.surrounding()}')
print(f'circle2 area is {c2.area()}, circle surrounding is {c2.surrounding()}')
