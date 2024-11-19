'''
students = {
     '120' : {
          'name'    : 'muhammed',
          'surname' : 'kahveci',
          'phone'   : '5445447756'
     },
     '121': {
          'name'    : 'ahmet',
          'surname' : 'gozupek',
          'phone'   : '5345663142'
     },
     '122': {
          'name'    : 'unal',
          'surname' : 'turan',
          'phone'   : '5325661212'
     }
}  '''


# 1 bilgileri verilen ogrencileri kullanicidan aldiginiz bilgilerle saklayiniz
# 2 ogrenci numarasi ile sorgulama yap


students = {}

"""for i in range(3):
    name = input("student name: ")
    surname = input("student surname: ")
    phone = input("student phone: ")
    studentNo = i 

    students.update({
        i+1: {
            'name': name,
            'surname': surname,
            'phone': phone
        }
    })



** buradaki student isimleri degismiyor butun listeyi bu sekilde veremedim 
'''for x in range(3):  
    x += 1 
    print(f"Student NO is {x}, student is {name} {surname}. Student phone is {phone}")
    print("*** " * 5)'''

print(students)

sorguNo = input('sorgulanacak numara : ')

find_student  = students[sorguNo]
print(find_student)
"""

students = {}

studentNo = input("STUDENT NUMBER: ")        #    student 1 info
name = input("student name: ")
surname = input("student surname: ")
phone = input("student phone: ")


students.update({
     studentNo: {
          'name': name,
          'surname': surname,
          'phone': phone
        }
    })

studentNo = input("STUDENT NUMBER: ")        #    student 2 info
name = input("student name: ")
surname = input("student surname: ")
phone = input("student phone: ")


students.update({
     studentNo: {
          'name': name,
          'surname': surname,
          'phone': phone
        }
    })
print("**** " * 5 )
print(students)
print("**** " * 5 )

findStudent = input('Sorgulanacak stundent no: ')
print(students[findStudent])

student = students[findStudent]
print(f"Student NO is {findStudent}, student is {student['name']} {student['surname']}. Student phone is {student['phone']}")
print("*** " * 5)










