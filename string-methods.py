message = 'hello there. my name is Emir'

#message = message.upper()      #.upper() tüm harfleri büyük yapar.
#message = message.lower()      #.lower() tüm harfleri küçük yapar.
#message = message.title()      #.title() tüm kelimelerin sadece baş harfi büyük olur.Diğer harfler küçüğe çevrilir.
#message = message.capitalize() #.capitalize() tüm metnin yalnızca en başındaki ilk harfini büyük yapar,geri kalan tüm harfleri ise küçük yapar.
#message = message.strip()      #.strip() bir metnin başındaki ve sonundaki bütün boşlukları siler,ortaya ve aralara dokunmaz.
#message = message.split()       #.split() metni belirlediğin yerlerden bölüp liste yapar. ['hello', 'there.', 'My', 'name', 'is', 'Emir', 'Gürbüztürk']
#message = message.split('.')     #parantezin içine yazdığımız işarete göre ayırdı. ['hello there', ' My name is Emir Gürbüztürk']
#dolayısıyla başlandaki indeks sayısı 2 ye düşmüş oldu. } print(message[1]) çıktısı my name is Emir olur indeksler 0 dan başlar.
#message = '-'.join(message)   #.join birleştirme işlemi yapar ve birleştirirken istediğimiz elemanları aralara atabiliriz.
# çıktı}hello-there.-my-name-is-Emir

"""
index = message.find('Emir')
print(message)
print(index)     # çıktı} "24" 24.harf indeksi E ye eşitmiş aslında bu kelimenin geçtiğini anlamış olabiliyoruz.
 'Emirr' yazsaydık çıktı -1 geecekti yani aslında -1 bu kelimenin çıktıda bulunmadığını ifade eder.
"""


"""
isFound = message.startswith('h')     #kelimenin başladığı ilk harf girdi ile aynı ise true yanlış ise false yanıtını verir. 
# yani .startwith komutu paragrafın ilk başladığı harfi anlamak için kullanılır.
print(isFound)   çıktı } True
"""


"""
isfound = message.endswith('r') çıktı true ancak boşluk ve iaretlere dikkat et

print(isfound)
"""


"""
#message = message.replace('Emir', 'Berat')    
#bu metot girdideki doğru kelimeyi yazdığınızda onun yerine başka bir metin yazmanıza yardımcı olmaktadır.
 
message = message.replace('Emir', 'Berat').replace(' ','^^').replace('e','q')
çıktı } hqllo^^thqrq.^^my^^namq^^is^^Bqrat

print(message)
"""

#message = message.center(100)      #girdiğimiz girdiyi 100brim alan içerisine girdiyi ortalayarak yazar.
#çıktı                                     hello there. my name is Emir        
                 
message = message.center(50,'"')   #integer olduğu için tırnak içine alınarak yazılamıyor.
print(message)