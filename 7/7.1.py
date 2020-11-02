#kelime heceleme programi

cumle =""
kelime=""

sablonlar = ['1','01','10','010','100','0010','0100','00100']

kelime = "010100101"

hecelenmis = ""

yeniliste = []

for eleman in sablonlar:
   if eleman == kelime [len(hecelenmis):len(hecelenmis)+len(eleman)]:
      yeniliste.append(eleman)
      yeniliste.reverse()


for eleman2 in yeniliste:
   if kelime[len(eleman2)] =='0':
      hecelenmis+=(eleman2)
    

   
print yeniliste



      












