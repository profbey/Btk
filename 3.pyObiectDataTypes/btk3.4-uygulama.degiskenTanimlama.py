"""
 1- Bir musterinin asagidaki bilgileri icin degisken olustur.

 musteri adi 
 musteri soyadi 
 musteri ad + soyadi 
 musteri cinsiyeti
 musteri tc kimlik no 
 musteri dogum yili 
 musteri adres bilgisi
 musteri yasi

"""
customerName = "murat"
customerSurname = "Gogebakan"
customerTotalName = customerName + " " + customerSurname
customerSex = True      #True = "Erkek"//Bu ifade 2 cesit olabilecegini dusundugu icin kullandi. 
customerID = 224421020524
customerDate = 1997
customerOld = 2024 - customerDate
customerLoc = "Dikimevi, Ankara"


"""
2- Asagidaki siparislerin toplam bilgisini hesaplayiniz.

siparis 1 => 110 TL
siparis 2 => 1005.85 TL
siparis 3 => 384.7 TL


"""
siparis1 = 110
siparis2 = 1005.85
siparis3 = 384.7 

siparisTotal = siparis1 + siparis2 + siparis3
print("siparis toplam: ", siparisTotal)