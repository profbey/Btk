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

rst = dir(re)
print(rst) 

