# -*- coding: cp1254 -*-
def topla():
   print 3+5
topla()


def topla2(a=1,b=2,c=3):
   d=a+b+c
   return d  

def topla3(x,y,z):
   t=x+y+z
   return t #bir fonksiyonun yaptigi seyi deger olarak dondurmesini istiyorsak return yazmak gerek
print topla3 (3,5,9)

aa =topla3(5,9,7)
print aa
print topla3(z=7,y=9,x=5)#boyle de yapilir
#eger boyle parametre vermeseydik 1. xe 2.y ye, 3. z ye giderdi

#print topla3(5,9,y=6) ya y yerine z yazicaktik yada hic isimlendirmicektik
#once isimlendirilmis olani yapar.Once y'ye aktari sonra x'e, sonrakini y ye aktaramaz cunku zaten bir deger var

#print topla3(x=3,y=6,9) buda hata. Once parametresiz degerler yazilmali sonradan parametreli degerler yazilmali
print topla2(a=6,c=2)


def yaz (*parametreler):  #bu sekilde tanimlarsak istedigimiz kadar parametre verebiliriz
   print parametreler     # * parametreleri 1 demet icerisine topluyor
yaz()
yaz(3)

yaz ('ali','veli')
yaz([3,4,6,7,'ali'])


def yaz2(*parametreler2):
#for x in range len(parametreler2)):
   adet = 0
   for x in parametreler2:
      if type(x) in [int,float]:
         adet+=1 #1 yerine x yazsak tolamlarini vericekti
   return adet

print yaz2(3,4,6,7,'ali')

def toplam(**parametreler): #** isimlendirilmis parametreleri alir
   print parametreler

toplam (x=3,y=5,z=7)

def yazbakalim(*pr1, **pr2):
   print pr1
   print pr2

yazbakalim (3,5,7,x=6,y=8,c=0.9)   
