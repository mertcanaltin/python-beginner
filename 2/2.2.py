x=()
print type (x)
#Tipini Tuple tanýmlayýp yazdýrdma

y =[]
print type(y)
#Liste tipinde bir deðiþken tanýmlayýp tipini yazdýrma

x=(4)
print (x)
print type (x)
#Böyle olunca tipi int tanýmlýyor

x=(4,)
print (x)
print type (x)
#Böyle olunca tipi tek elemanlý demet tanýmlýyor


meyve = "armut"
list(meyve)
print list (meyve)


a = "elma"
b = "armut"
c= "kiraz"
print list ((a,b,c))



print len(meyve)
#Listenin eleman sayýsýný verir

listem=[1,2,3,4,5,6,7,8,9]

print listem[0]
#Listenin ilk elemanýný verir

print listem[1:3]
#Listenin 1.den itibaren 2 elemanýný verir

print listem[1:]
#Listenin 1.den itibaren bütün elemanýný verir

a = [5,6]
a.append(7)
print a
#Listeye eleman ekleme
