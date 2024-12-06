'''
myList = [1,2,3,4]
myStr = 'my string'

print(len(myList))
print(len(myStr))
print(type(myList))
print(type(myStr))
'''

class Movie():
        def __init__(self,title, director, duration):
                self.title = title
                self.director = director
                self.duration = duration
                print('The movie object was made.') 
                
        def __str__(self) -> str:
                return print(f'{self.title} by {self.director}')
        
        def __len__(self) -> int:
                return self.duration
        
        def __del__(self):
                return print(f'The object deleted')

m = Movie('Movie Name','Director Name' ,120)

print(type(m))
print(len(m))
print(m)















