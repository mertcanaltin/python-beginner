# -*- coding: cp1254 -*-
sd = 0
sy = 0
sb = 0

td = 0
ty = 0
tb = 0

fd = 0
fy = 0
fb = 0

def 


sd = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")
sy = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")

td = input("Türkçe sınavındaki doğru sayınızı giriniz: ")
ty = input("Türkçe sınavındaki doğru sayınızı giriniz: ")

fd = input("Fen Bilimleri sınavındaki doğru sayınızı giriniz: ")
fy = input("Fen Bilimleri sınavındaki doğru sayınızı giriniz: ")
   
if 120 > (sd+sy):
   sb = 120 - (sd+sy)
else:
   print "Hatalı giriş lütfen tekrar giriniz"
   sd = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")
   sy = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")

if 120 > (td+ty):
   sb = 120 - (td+ty)
else:
   print "Hatalı giriş lütfen tekrar giriniz"
   td = input("Türkçe sınavındaki doğru sayınızı giriniz: ")
   ty = input("Türkçe sınavındaki doğru sayınızı giriniz: ")

if 120 > (fd+fy):
   sb = 120 - (fd+fy)
else:
   print "Hatalı giriş lütfen tekrar giriniz"
   fd = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")
   fy = input("Sosya Bilimler sınavındaki doğru sayınızı giriniz: ")   
   
print sd,sy,sb
   


