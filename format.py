name = "Emir"
surname = " Gürbüztürk"
age = 18
#print("my name is {} {}".format(name,surname))  # süslü parentezlerin sırasıyla 0,1,2,3 diye formatta karşılık bulan indeksleri vardır. normal
#sırasıyla ilerler ancak sen indekslerin yerini değiştirmek istersen süslü parantezlerin içersine indeks numarasını yazarak değiştirebilirsin.
#örnek
#print("my name is {1} {0}".format(name,surname))  # çıktı = my name is  Gürbüztürk Emir

#print("my name is {y} {x}".format(x=name,y=surname)) #bu şekilde değişkenlerdeki indekslerede değişken atayarak doğrudan süslü paranteze değişkeni yazabiliriz.


#print("my name is {} {} and l am {} years old".format(name ,surname,age)) # çıktı = my name is Emir  Gürbüztürk and l am18 years old

#print("my name is {} {} and l am {} years old".format(name,name,name))  # çıktı = my name is Emir Emir and l am Emir years old
"""
result = 200/500
print("the result is {} ".format(result)) #burada bir float değer çıkmış oldu. çıktı = the result is 0.4 

"""
#result = 200/700
#print("the result is {} ".format(result)) #ÇIKTI= the result is 0.2857142857142857 ancak sadece belirli küsüratı göstermek için aşşağıdaki işlem yapılır.

#print("the result is {x:1.4} ".format(x=result)) 
#1: Sayının ekranda kaplayacağı minimum karakter genişliğini belirler; sayı zaten bu boyuttan büyük olduğu için olduğu gibi görünür, ekstra boşluk eklenmez.
#4 (Hassasiyet): Virgülden sonraki kısmın kaç basamak uzunluğunda olacağını belirler. çıktı = the result is 0.2857

print(f"my name is {name} {surname} and l am {age} years old")