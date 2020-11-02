from math import *

def uzunluk(noktalar):
    sonuc = sqrt((noktalar[2]-noktalar[0])**2 + (noktalar[3]-noktalar[1])**2)
    return sonuc



def alan(ken1,ken2,ken3):
    u = (ken1+ken2+ken3)/2
    sonuc = sqrt(u*(u-ken1)*(u-ken2)*(u-ken3))
    return sonuc



k1 = uzunluk([100,100,200,150])
k2 = uzunluk([150,200,200,150])
k3 = uzunluk([150,200,100,100])
print k1, k2, k3

#bualan=alan(ken3 = k3,ken1 = k1,ken2 = k2)
bualan=alan(k1,k2,k3)
print bualan

rnokta = (200,180)  #150, 160

ku1k1 = uzunluk([100,100,150, 160])
ku1k2 = uzunluk([200,150,150, 160])
ku1k3 = uzunluk([200,150,100,100])

ku1a = alan(ku1k1,ku1k2,ku1k3)
print ku1a

ku2k1 = uzunluk([150,200,150, 160])
ku2k2 = uzunluk([200,150,150, 160])
ku2k3 = uzunluk([200,150,150,200])

ku2a = alan(ku2k1,ku2k2,ku2k3)
print ku2a

ku3k1 = uzunluk([150,200,150, 160])
ku3k2 = uzunluk([100,100,150, 160])
ku3k3 = uzunluk([150,200,100,100])

ku3a = alan(ku3k1,ku3k2,ku3k3)
print ku3a

kualantop = ku1a+ku2a+ku3a

if bualan - kualantop < 0.0001:
    print "hedef vuruldu"
else:
    print "karavana"

print bualan - kualantop

            


    
