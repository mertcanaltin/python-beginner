tek = []
cift = []
tumliste = []
while len(tumliste)<10:
   soru = input("Bir sayi gir ")
   if soru not in tumliste:
      tumliste.append(soru)
      if soru % 2 == 1:
         tek += soru,
      else:
         cift += soru, 
print "Tek sayilar",tek
print "Cift sayilar",cift
