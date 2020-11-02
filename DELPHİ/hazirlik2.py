def BilgiAl():
    #Sosyal ile ilgili kýsým
    sosyalD = input("Sosyal bilimlerin DOÐRU sayýsýný giriniz.")
    sosyalY = input("Sosyal bilimlerin YANLIÞ sayýsýný giriniz.")
    sosyalB = 0
    
    if sosyalD + sosyalY > 40:
        print "Yanlýþ veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        sosyalB = (40) - (sosyalD + sosyalY)
        gidenDogrularSos = sosyalY / 4.0
        sosyalD -= gidenDogrularSos
        sosyalY += gidenDogrularSos

    print "doðru ",sosyalD,"\r"
    print "yanlýþ ",sosyalY,"\r"
    print "boþ ",sosyalB

    #Turkce icin olan kisim
    turkceD = input("Türkçe DOÐRU sayýsýný giriniz.")
    turkceY = input("Türkçe YANLIÞ sayýsýný giriniz.")
    turkceB = 0
    
    if turkceD + turkceY > 40:
        print "Yanlýþ veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        turkceB = (40) - (turkceD + turkceY)
        gidenDogrularTurk = turkceY / 4.0
        turkceD -= gidenDogrularTurk
        turkceY += gidenDogrularTurk

    print "doðru ",turkceD,"\r"
    print "yanlýþ ",turkceY,"\r"
    print "boþ ",turkceB

    #Fen icin olan kisim
    fenD = input("Fen Bilimleri DOÐRU sayýsýný giriniz.")
    fenY = input("Fen Bilimleri YANLIÞ sayýsýný giriniz.")
    fenB = 0
    
    if fenD + fenY > 40:
        print "Yanlýþ veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        fenB = (40) - (fenD + fenY)
        gidenDogrularFen = fenY / 4.0
        fenD -= gidenDogrularFen
        fenY += gidenDogrularFen

    print "doðru ",fenD,"\r"
    print "yanlýþ ",fenY,"\r"
    print "boþ ",fenB


    #Hesaplama kismi
    toplamPuan = (sosyalD * 2.5) + (turkceD * 1.5) + (fenD * 2.0)
    print "Bu öðrencinin aldýðý toplam puan ==> ",toplamPuan
    
BilgiAl()
