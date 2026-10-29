"""
x = input("1.sayı: ")   #input(): Program çalışırken kullanıcıdan klavyeden veri almayı sağlar.
y = (input("2.sayı: "))
toplam = int(x) + int(y) 

print(type(x))
print(type(y))
print(type(toplam))

print(toplam)
"""



x = 5 #int
y = 1.3 #float
name = "çınar" #string(str)
isOnline = True #True ve False özel anahtar bool oldukları için büyük harf ile başlamalıdırlar


#print(type(x))
#print(type(y))
#print(type(name))
#print(type(isOnline))


#Type conversion

# int to float
#x = float(x)
#print(x)
#print(type(x))   # {class "float"} 5.0 int i float a çevirdik


#float to int
#y = int(y)
#print(y)
#print(type(y)) # {class "int"}  2 float ı int e çevirdik

#result = x + y
#print(result)
# print(type(result)) # {class "float"} 6.3 int + float = float

#result = str(x) + str(y)
#print(result)
#print(type(result)) #<class 'str'> 51.3 5 ve 1.3 -> 51.3


 #bool to str
#isOnline = str(isOnline)
#print(isOnline)
#print(type(isOnline)) # <class 'str'> True


#bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))



"""
    DAİRE ALANI =  πr²
    DAİRE ÇEVRESİ = 2πr

    *Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız (r: 3.14)

"""
pi = 3.14
r = float(input("yarı çap: "))
alan = pi * r ** 2
cevre = 2 * pi * r
#print("alan:" , alan)
#print("çevre:" , cevre)

print("alan: " + str(alan) + " çevre: " + str(cevre))
