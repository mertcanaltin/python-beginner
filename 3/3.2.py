s = {}
devam = True
while devam:
   anahtar = raw_input('Anahtar giriniz: ')
   if s.has_key(anahtar):
      deger = raw_input ('Deger giriniz: ')
      if deger not in s[anahtar]:
         s[anahtar] = (s[anahtar],deger)
   else:
      s[anahtar] = (raw_input('Deger giriniz: '),)
   if raw_input ('Devam edecekmisiniz (E / H): ') == 'H':
      devam = not devam
print s      



