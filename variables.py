maasEmir = 3000
maasYusuf = 4000
maasBerat = 5000
vergi = 0.25
print(maasEmir - (maasEmir*vergi))
print(maasYusuf - (maasYusuf*vergi))
print(maasBerat - (maasBerat*vergi))


# Değişken Tanımlama Kuralları

# rakam ile başlayamaz 
number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)


# Büyük küçük harf duyarlılığı vardır

age = 20
AGE = 30

print ( age)
print (AGE)


# Türkçe karakter kullanmayalım

yas = 20
_age = 20

x = 1           #int
y = 2.3         #float
name  = "çinar" #string
isStudent = True #bool

a = "10"
b = "20" 
print( a+b) # sonuç 1020 yani tırnak işareti ifadeleri birleştirir

firstname = "Emir" 
lastname = " Gürbüztürk" 
print (firstname+lastname)