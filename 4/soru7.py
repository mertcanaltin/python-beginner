iller = ["ADANA","ADIYAMAN","AFYON","AGRI","AMASYA","ANKARA","ANTALYA","ARTVIN","AYDIN","BALIKESIR",
"BILECIK","BINGOL","BITLIS","BOLU","BURDUR","BURSA","CANAKKALE","CANKIRI","CORUM","DENIZLI","DIYARBAKIR","EDIRNE","ELAZIG","ERZINCAN",
"ERZURUM","ESKISEHIR","GAZIANTEP","GIRESUN","GUMUSHANE","HAKKARI","HATAY","ISPARTA","MERSIN","ISTANBUL","IZMIR","KARS","KASTAMONU","KAYSERI",
"KIRKLARELI","KIRSEHIR","KOCAELI","KONYA","KUTAHYA","MALATYA","MANISA","KAHRAMANMARAS","MARDIN","MUGLA","MUS","NEVSEHIR","NIGDE",
"ORDU","RIZE","SAKARYA","SAMSUN","SIIRT","SINOP","SIVAS","TEKIRDAG","TOKAT","TRABZON","TUNCELI","SANLIURFA","USAK","VAN","YOZGAT","ZONGULDAK",
"AKSARAY","BAYBURT","KARAMAN","KIRIKKALE","BATMAN","SIRNAK","BARTIN","ARDAHAN","IGDIR","YALOVA","KARABUK","KILIS",
"OSMANIYE","DUZCE","YURTDISI"]

#for i in range (0,82):
#   print i+1," = ",iller[i]
baslik = "Iller ve plaka numaralari"
print (baslik.upper()).center(110)
for i,j in enumerate(iller): #enumeratenin yaptigi is= i,j =(0,Adana) seklinde yapiyor. i ye 0, j ye adana
   #print i+1,j
   
   print str(i+1).rjust(3),"=",j.rjust(13),
   if (i+1) % 6 ==0:
      print
   
