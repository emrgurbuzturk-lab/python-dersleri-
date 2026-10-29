website= "http://www.sadikturan.com"
course= "python kursu: Baştan sona python programlama rehberimiz (40 saat)"

# 1-'course' karakter dizisinde kaç karakter bulunmaktadır?
x=len(course)

# 2-'website' içinde www karakterlerini alın.
y=website[7:10]
# 3-'website' içinden com karakterlerini alın.
z=website[-3:]
# 4- 'course' içinde ilk 15 ve son 15 karakterlerini alın.
a=course[0:15]
b=course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
c=course[::-1]
#ek bilgi
d = "12345" * 4
print(d[::5])
name,surname,age,job = 'bora','yılmaz',32,'mühendis'

# 6- yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#    'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.'

f ="benim adım " + name +" "+ surname + ", yaşım "+ str(age) + " ve mesleğim "+ job + "."
t =  'Benim adım {} {}, yaşım {} ve mesleğim {}.'.format(name,surname,age,job) # indeksler formatın içindeki değerlerden itibaren 0,1,2... devam eder.
g =  'Benim adım {3} {1}, yaşım {2} ve mesleğim {0}.'.format(name,surname,age,job)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
l = 'Hello world'
l = l[0:6] + "W" + l[7:]

# 8- 'abc' ifadesinin yan yana 3 defa yazdırın.
p= "abc" * 3

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(f)
print(t)
print(f"Benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis.")
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")
print(g)
print(l)
print(p)