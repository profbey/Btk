x = 5 
result = 5 < x < 10 
print(result)

# AND OPERATOR = iki kosulun True olmasi gerek

result1 = x > 4 and x < 10              # True,  True => True 
print(f'result 1 degeri = {result1}')

result2 = x > 5 and x < 10              # False, True => False
print(f'result 2 degeri = {result2}')


hak = 5 
devam = "e"

result3 = (hak > 3 ) and (devam == "e")

print(f'result 3 degeri = {result3}')


# OR OPERATOR  = iki degerden birinin True olmasi yeterli

result4 = (x > 0 ) or (x % 2 == 0)      # True,  False => True
                                        # False, True  => True
                                        # False, False => False

print(f'result 4 degeri = {result4}')




# NOT OPERATOR = cevabi tersine cevirir

result5 = not (x > 0 )                  # False => True
print(f'result 5 degeri = {result5}')   # True  => False
















