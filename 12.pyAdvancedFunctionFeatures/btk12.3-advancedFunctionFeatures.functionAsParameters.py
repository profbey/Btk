def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b 
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b


def islem(f1,f2,f3,f4,islem):
    if islem == 'toplama':
        print(f1(1,1))
    elif islem == 'cikarma':
        print(f2(5,3))
    elif islem == 'carpma':
        print(f3(4,1))
    elif islem == 'bolme':
        print(f4(25,5))
    else:
        print('invalid request...')

islem(toplama, cikarma, carpma,bolme,'toplama')
islem(toplama, cikarma, carpma,bolme,'cikarma')
islem(toplama, cikarma, carpma,bolme,'carpma')
islem(toplama, cikarma, carpma,bolme,'bolme')
