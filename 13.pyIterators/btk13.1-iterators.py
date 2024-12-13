lst = ['a','b','c']

for i in lst:
    print(i)



iterator = iter(lst)

# print(iterator)           # <list_iterator object at 0x000001829C0B7970>

# print(next(iterator))       # a
# print(next(iterator))       # b
# print(next(iterator))       # c
# print(next(iterator))       # error -> StopIteration

while True:                             # These all codes == for i in lst: print(i)
    try:                                # The for loop do that
        element = next(iterator)
        print(element)
    except StopIteration:
        break



## Why we do? Why we learn 
## We may want to create a class like list ourselves. In this case, we can use an iterator.

class myNumb:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start  += 1
            return x 
        else:
            raise StopIteration

lst = myNumb(30,20)

while True:                             # for i in lst: print(i)
    try:                                
        i = next(lst)
        print(i)
    except StopIteration:
        break
