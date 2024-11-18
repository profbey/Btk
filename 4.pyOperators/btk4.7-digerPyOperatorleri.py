# IDENTITY OPERATOR: 'IS' / 'IS NOT'

x = y = [1,2,3,4]
z =     [1,2,3,4]

print(z == x or z == y )            # Value    degerleri ayni oldugu   icin [Output = True]
print(x is z or y == z )            # Referans degerleri ayni OLMADIGI icin [Output = False]



# MEMBERSHIP OPERATOR: 'IN'

a = ['apple', 'banana']

print('banana' in a)               # Value degerinin listenin icinde olup olmadigini kontrol eder. [Output = False]

























