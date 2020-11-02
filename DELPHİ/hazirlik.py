kayitListesi = {};



def KayitGir():
    numarasi = raw_input("Numarasý : ")
    adiSoyadi = raw_input("Adý Soyadý : ")
    bolum = raw_input("Bölümü : ")
    
    matVize = raw_input("Matematik Vize Notu : ")
    matFinal = raw_input("Matematik Final Notu : ")

    FizikVize = raw_input("Fizik Vize Notu : ")
    FizikFinal = raw_input("Fizik Final Notu : ")

    KimyaVize = raw_input("Kimya Vize Notu : ")
    KimyaFinal = raw_input("Kimya Final Notu : ")

    global kayitListesi
    
    kayitListesi[numarasi] = {"adSoyad":adiSoyadi,"bolum":bolum,"matV":matVize,"matF":matFinal,"fizV":FizikVize,"fizF":FizikFinal,"kimV":KimyaVize,"kimF":KimyaFinal}
    IslemSor()


def KayitGoruntule():
    print "Görüntüleye geldiniz! \n \r"
    kisi = raw_input("Görüntülemek istediðiniz kullanýcýnýn numarasý giriniz : ")

    global kayitListesi

    bulundumu = "hayýr"
    
    for key,val in kayitListesi.items():
        if key == kisi: ## and val == kisi:
            print "Numarasý".ljust(15),":" , kisi,"\r"
            print "Adý Soyadý".ljust(15),":" , val["adSoyad"],"\r"
            print "Bölümü".ljust(15),":" , val["bolum"],"\r"
            
            print "Sýnav Notlarý \r"
            
            print "Matematik".ljust(15),val["matV"].ljust(5),val["matF"].ljust(5),"\r"
            print "Fizik".ljust(15),val["fizV"].ljust(5),val["fizF"].ljust(5),"\r"
            print "Kimya".ljust(15),val["kimV"].ljust(5),val["kimF"].ljust(5),"\r"
                        
            
            bulundumu = "evet"

    if bulundumu == "hayýr":
        print "aranan kiþi bulunamadý !"
    IslemSor()



def IslemSor():
    islem = raw_input("Kayit girmek için 'k' , kayit görüntülemek için 'g' yazýnýz.")
    if islem == "k":
        KayitGir()
    elif islem =="g":
        KayitGoruntule()
    else:
        print "Lütfen geçerli bir giriþ yapýnýz."
        IslemSor()




if kayitListesi == {}:
    print "Programý yeni açtýðýnýz için kayýt öncelikle girmelisiniz!"
    print kayitListesi
    KayitGir()
    




