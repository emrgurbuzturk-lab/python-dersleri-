""""
müşteri adı
müşteri soyadı
müşteri ad + soyad
müşteri cinsiyet
müşteri tc kimlik 
müşteri doğum yılı
müşteri adres bilgisi
müşteri taşı
"""
musteriAdi = "Emir"
musteriSoyadi = "Gürbüztürk"
musteriAdSoyad = "Emir Gürbüztürk" # yada musteriAdi + " " + musteriSoyadi *unutma değişkenler tırnak isaretine alınmaz.
musteriCinsiyeti = "erkek" # yada istersek true folse atayarak doğrudan komutlaştırabiliriz.
musteriTcKimlik = "72613128426" # buralarda string kullanırız çünkü bizden sayısal bir işlem için değer istemez.
musteriDogumYılı = 2008
musteriAdresi = "İstanbul Kadıköy"
musteriYasi = 2026 - musteriDogumYılı

"""
   2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
      sipariş 1 =} 110    TL
      sipariş 2 =} 1100.5 TL
      sipariş 3 =} 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3
print("total:", total)