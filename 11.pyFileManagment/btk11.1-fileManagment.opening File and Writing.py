# Dosya acmak ve olusturmak icin open() fonskiyonu kullanilir. 
# Kullanimi: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayi hangi amacla actigimizi belirtir.


# "w": (write) yazma modu. Dosyayi konumda olusturur.
#         ** Dosyayi konumda olusturur.
#         ** Dosya icerigin TAMAMINI siler ve yeniden ekleme yapar
'''
file = open('newFile.txt','w')
file = open('C:/Users/User/Desktop/newFile.txt','w')
file.close()


file = open('C:/Users/User/Desktop/newFile.txt','w',encoding='utf-8')
file.write('Whatever you say here, it writes to the file.\n')
file.close()
'''

# "a": (append) ekleme modu. Dosya konumda yoksa olusturur.
'''
file = open('C:/Users/User/Desktop/newFile.txt','a',encoding='utf-8')
file.write('Whatever you say here, it appends to the file.\n')
file.close()
'''

# "x": (create) olusturma modu. Dosya zaten varsa hata verir.
file = open('C:/Users/User/Desktop/newFile2.txt','x',encoding='utf-8')
file.write('If the file does not exist, it works. If the file exists, it gives an error\n')
file.close()

file = open('C:/Users/User/Desktop/newFile2.txt','x',encoding='utf-8')
file.write('FileExistsError: [Errno 17]')
file.close()


# "r": (read) okuma modu varsayilan. Dosya konumunda yoksa hata verir. 







 












