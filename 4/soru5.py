not1 = input('Ilk notu giriniz:')
not2 = input('Ilk notu giriniz:')
not3 = input('Ilk notu giriniz:')

toplam = not1*0.3 + not2*0.3 + not3*0.4
if toplam < 60:
   print "Notunuz",toplam,". Kaldiniz"
else:
   print "Notunuz",toplam, "Gectiniz"
 # yada

ort = 0
oranlar = [0.30,0.30,0.40]
for i in range(3):
   ort += input(str(i+1)+' . sýnav notu: ') * oranlar[i]
if ort < 60:
   print "kaldi"
else:
   print "gecti"                
                
