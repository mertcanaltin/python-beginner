for i in dir(str):
   if "_" not in i:
      print i

a = "arinoksas"
b = "arin5oksas"
c = "12345"
d = "ARIN"
e = " "
f = "arin oksas"
g = "1234567"
h = ["Ali","Veli","Deli"]
print "-----------"
print a.capitalize()
print a.count('s')
print a.endswith("a")
print a.endswith("sas")
print a.find("as")
print a.find("n",5,8)#(virguldeki rakam kacinci indexten aramaya baslicagi
#-1 sonu veriyosa yok demek
print a.index("n",1,8) #bunla arattigimizda bulamayinca hata veriyor
print a.isalpha()
print b.isalnum()
print c.isdigit()
print d.isupper()
print e.isspace()
print f.title() #basliga cevirir
print g.join(h)
print g.isspace.__doc__
print f.replace("a","sss",2)#son yazdigimiz rakam kadar "a" yi degistirir
print d.swapcase()
print g.zfill(10)
print f.rjust(30) #saga 30 karakter ilerletiyor
print a.ljust(10), g
print f.rjust(20,"#"), "selam"
