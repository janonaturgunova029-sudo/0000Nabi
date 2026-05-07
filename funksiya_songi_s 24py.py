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

def daraja2(x): # Istalgan x sonini kvadratini qaytaradi
        """Berilgan sonni kvadratini qaytaruvchi funksiya"""
        return x*x

print(list(map(daraja2,sonlar)))








