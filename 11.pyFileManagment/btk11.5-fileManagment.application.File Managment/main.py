def ortalamaHesapla():
    print(' notlar '.center(50,'*'))

    try:
        with open('sinavNotlari.txt', 'r', encoding='utf-8') as file:
            for satir in file:
                print(notHesapla(satir))
    except FileNotFoundError:
        print("Error: 'sinavNotlari.txt' file not found. Please create the file or check the file path.")

def notHesapla(satir): # Add satir as argument
    satir = satir[:-1]
    lst = satir.split(':')
    s_name = lst[0]
    s_grade = lst[1].split(',')

    mt1 = int(s_grade[0])
    mt2 = int(s_grade[1])
    mt3 = int(s_grade[2])

    ort = int(((mt1+mt2)*(0.3))+(mt3 * 0.4))

    if ort >= 90:
        harf = 'AA'
    elif ort >= 85: 
        harf = 'BA'
    elif ort >= 80:
        harf = 'BB'
    elif ort >= 75:
        harf = 'CB'
    elif ort >= 70:
        harf = 'CC'
    elif ort >= 65:
        harf = 'DC'
    elif ort >= 60:
        harf = 'DD'
    elif ort >= 50:
        harf = 'FD'
    else:
        harf = 'FF'
    return s_name + ':' + harf + '\n'
        

def not_gir():
    name = input('student name: ')
    surname = input('student surname: ')
    mt1 = input('midterm 1: ')
    mt2 = input('midterm 2: ')
    mt3 = input('final grade: ')

    with open('sinavNotlari.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname}:{mt1},{mt2},{mt3}\n')

def not_kaydet():
    with open('sinavNotlari.txt', 'r', encoding='utf-8') as file:
        lst = []
        for i in file:
            lst.append(notHesapla(i)) # Changed to use parentheses for append
        with open('harfNotlari.txt', 'w', encoding='utf-8') as file2:
            for i in lst:
                file2.write(i)

while True:
    try:
        islem = input('1) notlari oku \n2) not gir \n3) Harf notunu disa aktar \n4) cikis \nSecim: ')
    except Exception:
        False
    
    if islem == '1':
        ortalamaHesapla()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        not_kaydet()
    elif islem == '4':
        print('kaydedildi')
        break
    else:
        False