#btk ders 1 - net maas hesaplama kodu - ek input fonksiyonu kullanildi.

kullanici1 = float(input("sayi girin ", ))
vergiOrani = float(input("vergi orani girin ", )) / 100

netMaas = float(kullanici1 - (kullanici1 * vergiOrani))
print(netMaas)

# Devaminda bir excel dosyasi olusturup bunu bir database olarak kullanacagim.
# Sonrasinda ise belirli miktar ustundeyse farkli vergi oraninda hesap yapilacak. 
# Boylece vergi orani kullanicidan istenmesine gerek kalmayacak. 
 

# Ek olarak, bu bir panel uzerinden yapilabilecek. 
# bu veri tabanina kullanici eklemek icin veya maas degisikligi yapmak icin kullanilabilecek diye dusunuyorum.