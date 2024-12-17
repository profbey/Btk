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




###### re module

strEx= 'Python Course: "Zero To Hero" Guidline With Profbey | 60+ hours'



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

