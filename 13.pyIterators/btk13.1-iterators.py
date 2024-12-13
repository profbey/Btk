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


