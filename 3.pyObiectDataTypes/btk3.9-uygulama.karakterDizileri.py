website = "http://www.sebnemferah.com"
course  = "Pyhton kursu: Bastan baslamak gerek bazen"

# course karakter dizisinde kac karakter bulunmaktadir
print(int(len(course)))

# website icinde www karakterlerini alin
print(website[7:10])

# website icinden com karakterlerini alin
print(website[-3:])

# course icinden ilk 15 ve son 15 karakteri alin 
print(course[:14])
print(course[-15:])

# course ifadesinin karakterlerini tersten yazdirin
print(course[::-1])
 
name, surname, age, job = 'bora', "yilmaz", 31, "engineer"

# yukaruda verilen degiskenler ile ekrana : "my name is bora yilmaz and, i am an engineer at 31 years old"
print(f'my name is "{name} {surname}" and, i am an {job} at {age} years old')

# "Naber ulan" ifadesindeki u harfini "U" ile degistirin 
a = "Naber ulan"
a = a.replace('u','U')
print(a)

# 'abc' ifadesini yan yana 3 kere yazdirin 
a = 'abc' *3
print(a) 