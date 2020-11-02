# -*- coding: cp1254 -*-
import math
import timeit
##def f(x):
##   return math.sqrt(x)
##bellekte yer tutar

##f = lambda x : math.sqrt(x) 
##bellekte yer tutmaz


fonk = lambda x,y :x+y
print fonk (3,5)
print fonk('ali','veli')


f2 = lambda *p : sum(p)
#sum verdigimiz parametrelerin toplamini bulur
# tek * la tanimladigimizdademet haline getiriyodu
# 2 * la yaptigimizda sozluk olarak algiliyodu
print f2(1,2,3,4,5)

f3 = lambda x, n = 2 : x**n
print "sonuc 1 = ",f3(5)
print "sonuc 2 = ",f3(2,4)
#n e deger vermezsek 2 olarak kullaniyor, verirsek verdigimizi kullanir

fnliste = [lambda x,n = n : x**n for n in [4,5,6,7]]
print fnliste[2](5)

fnliste = [lambda x,n = n : x**n for n in range(10)]
print fnliste[2](5)


print map(lambda x : x**2, (4,5,6,2,7))
print map(lambda x : x**2, [4,5,6,2,7])
print [x**2 for x in [4,5,6,2,7]]


print map(lambda x : x.upper(),"arin")
print map(lambda x : x.upper(),("arin","oksas"))
print [x.upper() for x in "arin"]

##print timeit.timeit("[x**2 for x in range(10)]")
##print timeit.timeit("map(lambda x : x**2,range(10))")

print [x for x in [6,1,8,11,5,-5,9] if x<9 and x>=5]
#filtreleme liste kurma yontemiyle

print filter (lambda x: x<9 and x>=5, [6,1,8,11,5,-5,9])
#buda filtreleme

print map(lambda x,y :x*y,("a","b","c","d"),(2,5,4,6))

print reduce (lambda x,y : x*y, (5,2,7,-2))
print reduce (lambda x,y : x+y, (5,2,7,-2))
print reduce (lambda x,y :10*x+y, [1,2,3,4,5])
#reduce once ilk 2 yi aliyor sonra bu 1. parametre 3. yu 2. parametreye sonra bunu 1. parametre 4. yu 2. parametre

def ff(x):
    return 4*x*(1-x)
x=0.125
print ff(x), ff(ff(x)), ff(ff(ff(x)))

#yukardakiyle bu ayni
print reduce (lambda x,y : y(x), [ff]*3, 0.125)


print reduce (lambda x,y : x*y, range(1,6))
#5faktoriyel

print reduce (lambda x,y : x+y, range(1,101))
#1den 100e kadar olan sayilarin toplami





































