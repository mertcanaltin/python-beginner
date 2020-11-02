
#import math
#from math import *
from math import sqrt

#Sozluk kullanimi
x= 'yas'
y = 'uc deger'
z = 'arin'
b={'isim1':'ahmet', x :3, y:(2,3,9), 'Boy' : 1.57, z : 'arinokx'}

print b
#-------------------
#demete eleman ekleme
d1=()
d1 = 3,5
print d1
#icinde eleman olan demete veri ekleme
d1 += 8,9 # d1 = d1 + 8,9
print d1
# demete tek eleman ekleme
d1 += 15, #, sayesinde ekliyor
print d1

#-------------------
#listeye eleman ekleme
l1 = []
l1=[3,5]
print l1
#listeye tek eleman ekleme
l1 += 15,
print l1
#icinde eleman olan listeye veri ekleme
l1 += 8,9 # l1 = l1 + 8,9
print l1

#--------------------
#for kullanimi
for i in range (3,6,1):
# range (3,6,1)3den 6 ya kadar 1er 1er =range (3)=[1,2,3]=['ali','veli','memo']= [5,9,7]
   print 'a'
#i deki elemanlari d listesine ekleyip yazdirma   
d=[]
for i in range (10):   
   d +=[i]
print d   
#i deki elemanlarin karesini d listesine ekleyip yazdirma   
d=[]
for i in range (10):   
   d +=[i**2]
print d  
#i deki elemanlarin ker kokunu d listesine ekleyip yazdirma 
d=[]
for i in range (10):   
   d +=[sqrt(i)] #eger sadece import math yapsakdik math.sqrt(i) yazmak zorundaydik
print d 










