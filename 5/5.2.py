def yazbakalim(*pr1, **pr2):
   print pr1
   print pr2

parametre = (4,7,9,2)
parametre2 = [4,7,9,2]
parametre3 = "selam arin"
parametre4 = {"x":4,"y":7,"z":9,"b":2}
yazbakalim(parametre)#boyle demet icinde demet yani tek elemanli demet
yazbakalim(*parametre) #boyle 4 elemanli demet yapti

yazbakalim(*parametre2)#yine ayni sekilde 4 elemanli demet yapti
yazbakalim(*parametre3)

yazbakalim (*parametre2,**parametre4)

