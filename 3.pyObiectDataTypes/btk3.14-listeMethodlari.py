numbers = [14,2,35,5,4,34,23,57,62]
letters = ['v','y','s','f','a','e','r','a','d','q',]

val_n = min(numbers)                    # kontrol kodu - BASLANGIC
val_l = max(letters)
len_numbers = len(numbers)    
len_letters = len(letters)
print(f'\n*BASLANGIC* numbers: {numbers} \nlen = {len_numbers}, \nmin val_n: {val_n} \ncount(2)   = {numbers.count(2)}'.title())
print(f'\n*BASLANGIC* letters: {letters} \nlen = {len_letters}, \nmax val_l: {val_l} \ncount("a") = {letters.count("a")}'.title())

 

numbers.append(49)            # dogrudan listenin sonuna ekler.
letters.append('p')

numbers.insert(3,99)          # indext numarasina gore ekleme yapar
letters.insert(2,'o')

numbers.sort()                # ifadeleri degerine gore siralar.
letters.sort()                # ifadeleri alfabeye gore siralar.

numbers.pop()                 # son elemani siler, indexleme ile calisabilir.
letters.pop(2)

numbers.remove(14)            # soylenilen elemani siler.
letters.remove("y")          

numbers.reverse()             # ifadeleri degerine gore TERSINE SIRALAR.
letters.reverse()



val_n = min(numbers)                    # kontrol kodu - FINAL
val_l = max(letters)
len_numbers = len(numbers)    
len_letters = len(letters)
print(f'\n*final* numbers: {numbers} \nlen = {len_numbers}, \nmin val_n: {val_n} \ncount(2)   = {numbers.count(2)}'.title())
print(f'\n*final* letters: {letters} \nlen = {len_letters}, \nmax val_l: {val_l} \ncount("a") = {letters.count("a")}'.title())


 
