#12- verileri bir liste halinde sakla.yeni liste elemanlarini ekrana yazdir **********Alternatif********

          #studentA: yigit bilgi   2010, (70,55,80)
          #studentB: bahadir sevgi 2005, (50,55,60)
          #studentA: ahmet arslan  2003, (46,56,89)


data = """
#studentA: yigit bilgi   2010, (70,55,80)
#studentB: bahadir sevgi 2005, (50,55,60)
#studentC: ahmet arslan  2003, (46,56,89)
"""
students = []
for line in data.split('#'):
  if line.strip():  # Boş satırları atlar
    student_info = line.strip().split(',')
    student_info = line.split()
    students.append(student_info)
print(f'\n* ex12 StudentKayit icindeki elemanlar : {students}')  
 
