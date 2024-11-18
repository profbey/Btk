message = "hello there. my name is Kilimcinin Koroglu"

message = message.upper()
message = message.lower()
message = message.title()      # her kelime basini buyuk harf yapar
message = message.capitalize() # sadece verilen str ifadenin ilk harfini buyuk harf yapar.

message = message.split('.')   # kume elemanlarini noktadan ayririp eleman olarak tanimlar. 
message = message.strip()      # bu eger verilen ifadenin basinda bosluk varsa onu silmeye yardimci olur.

message = message.split()      # her kelimeyi bir kume(dic) elemani olarak tanimlar.
message = ' '.join(message)    # ayrilan ifadeler arasina ne koymak istiyorsak onu tanimlayip birlestirir.

index = message.find('Kilicinin')     # bu str ifade icinde onun gecip gecmedigine bakar.
print(index)

isFound = message.startswith('b')     # Baslamasi 'b' ile baslayip baslamadigini sorar. True/False Question olarak degerlendirilir.
isFound = message.endswith('n')       # Bitisinin 'n' ile bitip bitmedigini sorar.      True/False Question olarak degerlendirilir.

message = message.replace('ğ','g').replace('ş','s').replace('ç','c').replace('ö','o').replace('ü','u').replace('ı','i') 
# bu satir tamamiyle turkce karakterleri ingilizce karakterler ile degistirir.

message = message.center(50,'*') # bu 50 karakterlik bir kume olusturur ve yazan mesaji tam ortada konumlandirir. sagina ve soluna * koyar.


 





### PROJE FIKRI: bu find ifadesi ve diger fonksiyonlari kullanarak Search_Engine isimli uygulama yapilacak.

### Method     : butun dosyalarin isimlerini log dosyasi altinda toplayacak.
# log dosyasi olmasi icin dosya adini message_n
# Buyuk/kucuk harf duyarliligi istemiyorsak .lower sonrasinda .split kullanacak.
# Sonra .find kullanilarak dosya bulunacak.
# Frakli bir seyde de bu arama metodunu kullanacaksak eger tum karakterleri .lower ile saklamak iyi olabilir. 


print(message)


