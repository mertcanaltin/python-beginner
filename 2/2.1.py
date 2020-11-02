def alan_hacim (YC):
   alan = 4 * 3.14* YC **2
   hacim = 4/3 * 3.14 * YC**3
   return alan,hacim
yaricap = input ("Lutfen Kurenin yaricapini giriniz: ")

ka,kh = alan_hacim(yaricap)
print ka, kh
##Bu þekilde ayrý ayrý tanýmlar

print alan_hacim(yaricap)
## Bu þekilde bir demet olarak sonuç döndürür

sonuc = alan_hacim(yaricap)
print sonuc
## Bu þekilde sonucu bir deðiþkene alýp öyle yazdýrdýk

print type(sonuc)
## Bu þekilde sonucun deðerini öðrendik
