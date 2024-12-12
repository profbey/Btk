# key -> value 

# 46 -> maras, 34 -> istanbul

cities = ['maras', 'istanbul']
plates = [46,34]

print(plates[cities.index('maras')]) # siralar uymasina ragmen kullanim anlaminda zor

plates_dic = {'maras': 46, 'istanbul': 34, 'ankara': 6}

print(plates_dic)

plates_dic['izmir'] = 35

print(plates_dic)

user = { 'cinar' : 36,
        'mustafa': 48,
        'ahmet'  : 31,

} # olarak kullanilabildigi gibi 

user_data = {
     'cinar' : {
          'age'     : 36,
          'roles'   : ['user'],
          'email'   : 'cinar43@gmail.com',
          'adress'  : 'dikimevi, ankara',
     },
     'mustafa' : {
          'age'     : 48,
          'roles'   : ['user'],
          'email'   : 'msutafababa44@gmail.com',
          'adress'  : 'ulus, ankara',
     },
     'ahmet': {
          'age'     : 28,
          'roles'   : ['admin', 'user'],
          'email'   : 'ahmethakan_46@gmail.com',
          'adress'  : 'birmingham, UK',
     }
}

print(user_data['cinar']) 
print(user_data['ahmet']['roles'])
