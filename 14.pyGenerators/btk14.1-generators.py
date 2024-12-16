# bellekte yer isgal etmeyen iterators icin kullanilir.
# bir liste icine kaydetme geregi duymuyorsak, sadece anlik lazimsa
# bu durumda o anda almak istedigimizde buradaki yield o an hesaplar
# o an hesaplar ve durur, lazim oldugunda bir kez daha islem yapar durur.
# bu bize anlik nokta atisi hesap yaptigi icin performans kazandirir.

'''
#* Normally
def cube(self):
    result = []

    for i in range(self):
        result.append(i**3)
    return result

print(cube(14))

'''
#* Alternative for optimizing

while True:
    try:
        x = int(input('whats the range?: '))
        break
    except Exception:
        False

def cube(self):
    for i in range(self +1):
        yield i ** 3

iterator = cube(x)

for i in iterator:
    print(i)


# generatorleri sadece fonksiyonlar icin mi olusturacagiz.
# tabiki hayir, comprehensive konusunda yaptigimiz gibi

lst = [i**3 for i in range(5)]  # bir liste tanimlanir, i**3 islemi yapip listeye ekler.
print(lst)                      

# ancak gelen sonucu bir generator olarak dondurmek istersek;

generator = (i**3 for i in range(1000))  # koseli parantez yerine normal parantez yaparsak bu generator objeye donusur

for i in generator:
    print(i)
