with open('newFile.txt', 'r+', encoding="utf-8") as file:   # r+ is for updating but overwrites.
          print(file.read())
          file.seek(0)
          file.write('deletes the index range of the thing to be written and writes over it')

with open('newFile.txt', 'r+', encoding="utf-8") as file:    
          file.seek(0)
          print(file.read())



# ************************************ Update at End of Page ************************************

with open('newFile.txt', 'a', encoding="utf-8") as file:
        file.write('\nSince we opened it with the "append" command, the write statement prints at the end of the page.')
             
with open('newFile.txt', 'r', encoding="utf-8") as file:   
          file.seek(0)
          print(file.read())



# *********************************** Update at Top of Page ************************************

with open('newFile.txt', 'r+', encoding="utf-8") as file:
        content = file.read()
        content = 'appending text\n' + content
        file.seek(0)
        file.write(content)  
            
with open('newFile.txt', 'r', encoding="utf-8") as file:   
          print(file.read())



# ************************************ Update at Middle of Page ************************************

with open('newFile.txt', 'r+', encoding="utf-8") as file:   
          lst = file.readlines()
          lst.insert(1,'appending at before of [1] item ')  # .insert -> insert object before index
          file.seek(0)

          for i in lst:                                     # to add dynamically and not to write the statement we added with insert to the file.
                  file.write(i)                             # ALTERNATIVE -> file.writelines(lst)
