# genel olarak bir arama sonucusunda calisir
# regular expression methodlari gelistirilebilir
# bir arama kriteri olsuturup bunu deneyebilirsin 
# mesela bir mail adres formati olusturup bunu kullanmak icin 
# kullanabilirsin/
# regular expression ifadeleri nasil yapilir? nasil kullanilir.

import re

dir_re = [
    'A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE',
    'M', 'MULTILINE', 'Match', 'NOFLAG', 'Pattern', 'RegexFlag', 'S',
    'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE',
    '_MAXCACHE2', '__all__', '__builtins__', '__cached__', '__doc__', 
    '__file__', '__loader__', '__name__', '__package__', '__path__', 
    '__spec__', '__version__', '_cache', '_cache2', '_casefix', '_compile',
    '_compile_template', '_compiler', '_constants', '_parser', '_pickle',
    '_special_chars_map', '_sre', 'compile', 'copyreg', 'enum', 'error',
    'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match',
    'purge', 'search', 'split', 'sub', 'subn', 'template'
]


strEx= 'Python Course: "Zero To Hero" Guidline With Proffbey | 60+ hours'



###### re module

#* re.findall() method

rst_find = re.findall('Python',strEx)
rstLen = len(rst_find)
print(f'finding rst: {rst_find}, len rst: {rstLen}\n')



#* re.split 

rst_split = re.split(' ', strEx)
rst_split = re.split('o', strEx)



#* re.sub()

rst_subStr = re.sub(' ','-',strEx)      # Python-Course:-"Zero-To-Hero"-Guidline-With-Profbey-|-60+-hours
rst_subStr = re.sub('/s','-',strEx)     # Python-Course:-"Zero-To-Hero"-Guidline-With-Profbey-|-60+-hours



#* re.search()                          # match objesi olarak dondurdu. ilk buldugu karsilasmanin degerlerini yazdirdi.

rst = re.search('Course',strEx)         # <re.Match object; span=(7, 13), match='Course'>

#rst = rst.span()                       # buldugu degerin indeks numaralarini verdi => (7, 13)
#rst = rst.start()                      # 7
#rst = rst.end()                        # 13
#rst = rst.group()                      # Course
#rst = rst.string                       # Python Course: "Zero To Hero" Guidline With Profbey | 60+ hours


###### regular expression 
'''
    [] -Koseli parantezler arasina yazilan butun karakterler aranir.

        [abc]   =>  a       : 1 match
                    ac      : 2 match
                    Python  : No matches

        [a-e]   =>  [abcde]
        [1-5]   =>  [12345]
        [0-39]  =>  [01239]

        [^abc]  =>  abc disindaki karakterler
        [^0-9]  =>  rakam olmayan karakterler
'''
rst = re.findall('[abc]',strEx)         # ['b']
rst = re.findall('[hour]',strEx)        # ['h', 'o', 'o', 'u', 'r', 'r', 'o', 'o', 'r', 'o', 'u', 'h', 'r', 'o', 'h', 'o', 'u', 'r']
rst = re.findall('[a-e]', strEx)        # ['e', 'e', 'e', 'd', 'e', 'b', 'e']
rst = re.findall('[0-5]', strEx)        # ['0']

rst = re.findall('[^abc]', strEx)       # ['P', 'y', 't', 'h', 'o', 'n', ' ', 'C', 'o', 'u', 'r', 's', 'e', ':', ' ', '"', 'Z', 'e', 'r',
                                        #  'o', ' ', 'T', 'o', ' ', 'H', 'e', 'r', 'o', '"', ' ', 'G', 'u', 'i', 'd', 'l', 'i', 'n', 'e',
                                        #  ' ', 'W', 'i', 't', 'h', ' ', 'P', 'r', 'o', 'f', 'e', 'y', ' ', '|', ' ', '6', '0', '+', ' ',
                                        #  'h', 'o', 'u', 'r', 's']


'''
    .  -Herhangi bir tek karakteri belirtir

        ..      =>  a       : No match
                    ab      : 1 match
                    abc     : 1 match
                    abcd    : 2 match   
'''
rst = re.findall('...',strEx)           # ['Pyt', 'hon', ' Co', 'urs', 'e: ', '"Ze', 'ro ', 'To ', 'Her', 'o" ',
                                        #  'Gui', 'dli', 'ne ', 'Wit', 'h P', 'rof', 'bey', ' | ', '60+', ' ho', 'urs']
rst = re.findall('Py..on',strEx)        # ['Python']


'''
    ^  -strEX belirtilen karakter ile basliyor mu?

        ^a      =>  a       : 1 match
                    abc     : 1 match
                    bac     : No match
'''
rst = re.findall('^a',strEx)            # []
rst = re.findall('^P',strEx)            # ['P']


'''
    $  -strEX belirtilen karakter ile bitiyor mu?
    
        a$      =>  a       : 1 match
                    lambda  : 1 match
                    Python  : No match
'''
rst = re.findall('s$',strEx)            # ['s']
rst = re.findall('t$',strEx)            # []
rst = re.findall('hours$',strEx)        # ['hours']


'''
    *  -Bir karakterin sifir veya daha fazla sayida olup olmadigini
        kontrol eder.
    
        ma*n    =>  mn      : 1 match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nin bitisiginde n yok)
'''
rst = re.findall('co*r',strEx)          # []
rst = re.findall('o*r',strEx)           # ['r', 'r', 'r', 'r', 'r']


'''
    +  -Bir karakterin sifir veya daha fazla sayida olup olmadigini
        kontrol eder.
    
        ma+n    =>  mn      : No match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nin bitisiginde n yok)
'''
rst = re.findall('o+u',strEx)           # ['ou', 'ou']


'''
    ?  -Bir karakterin sifir veya bir kez olmasini kontrol eder.
    
        ma?n    =>  mn      : No match
                    man     : 1 match
                    maaan   : 1 match
                    main    : No match (a'nin bitisiginde n yok)
'''
rst = re.findall('o?u',strEx)           # ['ou', 'u', 'ou']


'''
    {}  -Karakter sayisini kontrol eder.
    
        al{2}       =>  a karakterinin arkasina l karakteri 2 kez tekrarlanmali.
        al{2,3}     =>  a karakterinin arkasina l karakteri en az 2 en fazla 3 kere tekrarlanmali.
        [0-9]{2,4}  =>  en az 2 en cok 4 basamakli sayilar.                 
'''
rst = re.findall('f{2}',strEx)         # ['ff']
rst = re.findall('[0-9]{2,3}',strEx)   # ['60']


'''
    |  -OR ifadesidir, a yada b secekleri arasinda alternatif sunar.
    
        a|b     =>  cde     : No match
                    ade     : 1 match
                    acdbea  : 3 match
'''
rst = re.findall('o|u',strEx)           # ['o', 'o', 'u', 'o', 'o', 'o', 'u', 'o', 'o', 'u']


'''
    ()  -Gruplamak icin kullanilir.

        (a|b|c)xz   =>  a,b,c karakterinin arkasina xz karakterleri gelmeli.             
'''
'''
    \   -Ozel karakterleri aramizi saglar.
        \$a     =>  $ karakterlerinin arkasina a karakterini arar, yani 
                    $ regular expression engine tarafindan yorumlanmaz.

    \A  -Belirtilen karakter string in basina mi?
        \Athe   =>  'the' string in basinda mi

    \Z  -Belirtilen karakter string in sonunda mi 
        the\Z   =>  'the' string in sonunda mi

    \b  -Belirtilen karakter kelimenin basinda ya da sonunda mi?
        \bthe   =>  'the' kelimenin basinda mi?
        
'''
rst = re.findall(r'\APython',strEx)    # ['Python']
rst = re.findall(r'hours\Z',strEx)     # ['hours']
rst = re.findall(r'hours$',strEx)      # ['hours']

print(rst)
