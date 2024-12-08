try:
          file = open('C:/Users/User/Desktop/newFile1.txt','r',encoding='utf-8')
          print(file)
except FileNotFoundError:
        print('the file doesnt exist')
finally:
          file.close()



# with method -> islemin sonunda otomatik  olarak file.close() yapar.
# open('dosya', 'okunmaBicimi') as file -> file = open('dosya', 'okunmaBicimi')

with open('C:/Users/User/Desktop/newFile1.txt','r',encoding='utf-8') as file:
        content = file.read()
        print(content)

        file.seek(0)          # .seek(index number) -> okuma islemi sonrasi curser'i index numarasina gonderir
        print(file.tell())    # curser'in hangi konumda oldugunu soyler.
        
        content2 = file.read(10)
        print(content2)
