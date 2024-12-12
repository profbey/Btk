website = 'https://www.instagram.com'
course  = 'course: btk akademide yalandan python kursu rehberi (40 hours)'
number  = 4562

result = website.strip()
result = website.lstrip()
result = website.rstrip()



#* BASINDAKI VE SONUNDAKI GEREKSIZLERI KALDIRMA"

website = 'https://www.instagram.com'
# result = website.lstrip('https://www.').rstrip('.com') hatali kod cunku .rstrip yuzune output = instagra 

if result.startswith('https://www.'):
     result = result[12:]

if result.endswith('.com'):         # if statement True ise diger satira gider
     result = result[:-4]    
print(result)                       # output = instagram




result = course.upper()
result = course.lower()
result = course.title()

result = website.count('a')
result = website.count('www')
result = website.count('www', 0, 10) # bu ifade 0 ile 10. indext arasinda arar.

result = website.startswith("www")   # bool ifade, ouput = False
result = website.endswith('.com')

result = website.find('com')         # if statement is True, it give index number.
result = course.find('com')          # if statement is False, it give -1 because cannot give 0 and 0 number match to first character of the string 

result = "the format method is for function inside {}".format(number)


print(result)
