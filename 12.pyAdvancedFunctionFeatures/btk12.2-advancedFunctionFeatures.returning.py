def us_alma(number):              # f(x)
    # two = us_alm(2)
    # three = us_alm(2)

    def inner(power):
        return number ** power    # g(x)
    return inner 

powerOfTwo = us_alma(2)
print(powerOfTwo(3))              # h(x) = g(f(x)) => h(powerOfTwo(3)) = inner(us_alma(2), 3)
print('*'*50 + '\n')



def yetki_sorgula(page):
    
    def inner(role):
        if role == 'Amdin':
            return '{0} rolu {1} sayfasina ulasabilir'.format(role,page)
        else:
            return 'Access Denied.'
    return inner
        
user1 = yetki_sorgula('product edit')
print(user1('Amdin'))
print('*'*50 + '\n')



def islem(islemAdi):
    
    def topla(*args):
        topla = 0 
        for i in args:
            topla += i
        return topla
    
    def carp(*args):
        carp = 1
        for i in args:
            carp *= i
        return carp
    
    if islemAdi == 'topla':
        return topla
    elif islemAdi == 'carp':
        return carp

topla = islem('topla')
carp  = islem('carp')

print(topla(1,3,5,4,8,7,8))
print(carp(1,5,4,8,6,4,8,5,2,4))
