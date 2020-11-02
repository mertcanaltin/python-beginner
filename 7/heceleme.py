# -*- coding: cp1254 -*-
cumle = ""
kelime = "kaykay"
#kayserililerdenmisiniz
sablonlar = ['1','01','10','010','100','0010','0100','00100']

kelime = "010010"
#0100101010100100101010
hecelenmis = ""


while(True):
    yeniliste = []
    for eleman in sablonlar:
        if eleman == kelime[len(hecelenmis):len(hecelenmis)+len(eleman)]:
            yeniliste.append(eleman)
    yeniliste.reverse()
    for eleman2 in yeniliste:
        if kelime[len(eleman2)] == '0':
            hecelenmis+=eleman2+'-'
            break
    if len(hecelenmis)-hecelenmis.count('-')+1==len(kelime):
        break
print hecelenmis


