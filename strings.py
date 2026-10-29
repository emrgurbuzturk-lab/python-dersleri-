name = "Emir"
surname = "Gürbüztürk"
age = 18
greeting = "my name is " + name + " " + surname + " " + "and \nl am" + " " + str(age) + " " + "years old" # \n alt satırdan devam etmeyi sağlar.

print(greeting) 
print(greeting[0])
print(greeting[2])
print(greeting[7])
print(greeting[9]) # soldan sağa doğru 0,1,2,3,4... gider. sağdan sola doğru -1,-2,-3,-4...gider. stringteki kelimenin her harf elemanı bir indeks ile ifade edilir.
print(len(greeting))  # len ifadelerin kaç karakterden oluştuğunu söyler.
print(greeting[48]) # indeks 0 dan başladığı için karakter sayısı - 1 yapmalıyız yani son karakter 48 olmuş oldu. yada -1 sağdan basladığı için bu şekildede yapabiliriz.

print(greeting[2:10]) # ":" indeks aralığı belirlememizi sağlayarak o aralıktaki karakterleri alır.

print(greeting[3:]) # sayı yazmazsanız baştaki yazdığınız değerden sona kadar ele alır.

print(greeting[ :12]) # bu seferde sondak kullandığız değerden en başa kadar ele alır.

print(greeting[:]) # bu durumda ise komple tüm karakterleri ele alır.

print(greeting[2:20:2]) # bu ise 2 den 20 ye kadar 2 karakterden birini alarak ilerle anlamına gelmektedir.

