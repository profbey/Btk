""" *********************************************** list & dic & tuple farki ****************************************************************

Ozellik	                Liste (List)                        Sozluk (Dictionary)	                        Tuple


Tanim	                Sirali, değistirilebilir, 	        Sirasiz, değistirilebilir,                  Sirali, değistirilemez,  
                        indekslenebilir.                    anahtar-değer ciftlerinden olusur           indekslenebilir

Sira	                Korunur.	                        Korunmaz.	                                Korunur.

Değistirilebilirlik	    Evet. Elemanlar eklenebilir, 	    Evet. Hem anahtarlar hem de 	            Hayir. Elemanlar bir kere 
                        silinebilir/değistirilebilir.       değerler değistirilebilir.                  olusturulduktan sonra değistirilemez.

Erisim	                Indeks ile.                         Anahtar ile.Indexlenemez                    Indeks ile.

Gosterim	            Koseli parantez []	                Suslu parantez {}	                        Parantez ()

Kullanim Alanlari	    Sirali veri koleksiyonlari 	        Anahtar-değer iliskileri 	                Değistirilmemesi gereken verileri 
                        (orneğin, bir alisveris listesi).   (orneğin, bir kisinin bilgileri).           saklamak (orneğin, sabitler).

                        

Ornek Kullanim Alanlari

    Liste:
        Bir alisveris listesi olusturmak.
        Bir metindeki kelimeleri saklamak.
        Bir oyunun skorlarini tutmak.
    Sozluk:
        Bir kisinin bilgilerini (ad, soyad, yas) saklamak.
        Bir urunun ozelliklerini (ad, fiyat, stok) saklamak.
        Bir web sitesindeki kullanicilarin ayarlarini saklamak.
    Tuple:
        Koordinat: coordinate = (10, 20)
        Renk kodu: color = (255, 0, 0) (Kirmizi)
        Tarih: date = (2023, 11, 24)
        Fonksiyon parametresi: def hesapla(x, y): ... (x ve y bir tuple icinde de gonderilebilir)
        Sozluk anahtari: person = {("ad", "soyad"): ("Ali", "Veli")}
"""
