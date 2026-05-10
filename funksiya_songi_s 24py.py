# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:31:47 2026

@author: ASUS
"""
# nomsiz funksiyalar yaratish 


#def nom(argument):
#    return argument

#lambda argument1, argument2:ifoda
#import math 


#uzunlik=lambda pi,r:2*pi*r
#
#kvadrat=lambda x,y:x**y 
#print(kvadrat(3,5))


# LAMBDA ISHLATILADIGAN ORINLAR patdagi kodda lambda da yozilgan funksiya yasaydigan funkiya boladi



#def daraja(n):
#    return lambda x:x**n
#kvadrat=daraja(2)
#kub=daraja(3)

#print(f'3 ning kavdati {kvadrat(3)} ga teng, kubi esa {kub(3)} ga teng')
#from math import sqrt # sonning kvadrat ildizini hisoblayd
#sonlar=list(range(11))
#ildizlar=list(map(sqrt,sonlar)) # map 2 ta funksiyani oladi
#print(ildizlar)


#from math import sqrt
sonlar=list(range(15))
#ildizlar=list(map(sqrt,sonlar))
#print(ildizlar)
#import math

#def son(sqrt):
#    sonlar = list(range(0,15))
#    ildizlar = []
#    for son in sonlar:
#        ildizlar.append(sqrt(son))
#    return ildizlar

#print(son(math.sqrt))

#def daraja2(x): # Istalgan x sonini kvadratini qaytaradi
#        """Berilgan sonni kvadratini qaytaruvchi funksiya"""
#        return x*x

#print(list(map(daraja2,sonlar)))

#kvadratlar=list(map(lambda x:x*x,sonlar)) # buy yerda lambda funksiyasi orqalei 
# sonlar yaratilib sonlardagi qiymat x ga yuklanadi.

#from math import sqrt

#sonlar=list(range(13))
#ildizla=list(map(sqrt,sonlar))
#print(ildizla)

#sonlar=list(range())


#def daraja2(x):
#    """Berilgan sonning darajasini aniqlovchi funksiya"""
#    return x*x


#sonlar=list(range(1,17))
#print(list(map(daraja2,sonlar))) # BU YERDA FUNKSIYA YARATIB SHU FUNKSIYADA FOYDALANIB MEP BN SONLARNI BIRLASHTIRAYAPTI

#kvadrat=list(map(lambda x:x*x, sonlar))
#print(kvadrat)


#a=[4,5,8]
#b=[4,9,2]
#a_plus_b=list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)


#import random as r  #YANGI FILTER DEB ATALGAN FUNKSIYA 
#sonlar=r.sample(range(100),10)
#print(sonlar)
#def juftmi(x):
    
##    return x%2==0 #qoldiqni topish uchun shunday 2 % bolindi

#juft_sonlar= list(filter(juftmi,sonlar)) # HUDDI MAPDEK BIR FUNKSIYA VA QIYMAT QABUL QILIB SAALAB BERADI

#juft_sonlar=list(filter(lambda son: son%2==0,sonlar))
#print(juft_sonlar)



mevalar=['olma','anor','orik','gilos','limon','ananas','tarvuz']
#harf='a'
#mevalar_a=list(filter(lambda meva:meva.startswith(harf),mevalar))
#print(mevalar_a)

mevalar2=list(filter(lambda meva:len(meva)<=4,mevalar))
print(mevalar2)






