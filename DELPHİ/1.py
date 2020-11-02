# -*- coding: cp1254 -*-
ogrncno = []
ad = []
soyad = []
bolum = []
mat1 = []
mat2 = []
fizik1 = []
fizik2 = []
kimya1 = []
kimya2 = []
toplam = []
soru = "Hangisini yapmak istersin?\n Yeni kayit için 1'e basın\n Kayıtları görüntülemek için 2'ye basın\n Arama yapmak için 3'e basın \nCevap:"
cevap = input (soru)

if cevap == 1:
   ogrncno.append(input ("Lütfen Öğrenci numaranızı giriniz: "))   
   ad.append(raw_input ("Lütfen Adınızı giriniz: "))
   soyad.append(raw_input ("Lütfen Soyadınızı giriniz: "))
   bolum.append(raw_input ("Lütfen Bölümünüzü giriniz: "))
   mat1.append(input ("Lütfen Matematik 1.notunuzu giriniz: "))
   mat2.append(input ("Lütfen Matematik 2.notunuzu giriniz: "))
   fizik1.append(input ("Lütfen Fizik 1.notunuzu giriniz: "))
   fizik2.append(input ("Lütfen Fizik 2.notunuzu giriniz: "))
   kimya1.append(input ("Lütfen Kimya 1.notunuzu giriniz: "))
   kimya2.append(input ("Lütfen Kimya 2.notunuzu giriniz: "))
   print "***********************\n"
   cevap = input (soru)

if cevap == 2:
   print "***********************\n","ÖğrenciNo".rjust(15)+":",ogrncno
   print "Ad".rjust(15)+":",ad
   print "Soyad".rjust(15)+":",soyad
   print "Bolum".rjust(15)+":",bolum
   print "Mat1".rjust(15)+":",mat1
   print "Mat2".rjust(15)+":",mat2
   print "Fizik1".rjust(15)+":",fizik1
   print "Fizik2".rjust(15)+":",fizik2
   print "Kimya1".rjust(15)+":",kimya1
   print "Kimya2".rjust(15)+":",kimya2
   print "***********************\n"
   cevap = input (soru)
   
if cevap == 3:
   arama = input("Aramak istediğiniz öğrenci numarını giriniz: ")
   if arama in ogrncno:
      n = ogrncno.index(arama)
   print "***********************\n","ÖğrenciNo".rjust(15)+":",ogrncno[n]
   print "Ad".rjust(15)+":",ad[n]
   print "Soyad".rjust(15)+":",soyad[n]
   print "Bolum".rjust(15)+":",bolum[n]
   print "Mat1".rjust(15)+":",mat1[n]
   print "Mat2".rjust(15)+":",mat2[n]
   print "Fizik1".rjust(15)+":",fizik1[n]
   print "Fizik2".rjust(15)+":",fizik2[n]
   print "Kimya1".rjust(15)+":",kimya1[n]
   print "Kimya2".rjust(15)+":",kimya2[n]
   print "***********************\n"
   cevap = input (soru)
      
