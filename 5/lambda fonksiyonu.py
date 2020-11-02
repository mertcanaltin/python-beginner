##def f(x):
##   return x*x
#bu bellekte yer tutuyor
f = lambda x : x*x
print f(5),f(1.5),f(8.9)
#bu bellekten siliniyor, yer tutmuyor

def seritoplam(f,a,b):
   toplam = 0
   x = a
   while x <=b:
      toplam += f(x) # f(x) yerine x*x diyebilirdik
      x +=1
   return toplam   

print seritoplam(f,5,18)
