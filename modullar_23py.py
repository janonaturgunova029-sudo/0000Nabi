# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:24:36 2026

@author: ASUS
"""
# MODDULLARDA FOYDALANISHDAN MAQSAD YOZGAN KODLARIMIZNI YANADA TOZALASH. YZOGAN 
# FUNKSIYALARIMIZNI MANA SHU MODULLAR ICHIGA YASHIRIB QOYISH MAQSAD
# MODUL BU ALOHIDA FAYL KODNI BIR NECHA FAYLGA BOLADI BUNDAN MAQSAD UZUN KODLARNI ISHLATGANDA QIYNALMASLIK UN

#import avto_info_mod as aim # qisqa nom berish uchun shunday qilinad
#avto1=aim.avto_info('Gm','Malibu',"qora",'avtomat',2022,400000)
#aim.info_print(avto1)


#AGAR BUNDAN HAM QISQAROQ QILIB CHAQIRMOQCHI BOLSAK UNDA FROM DAN IMPORT QIL DEB CHAQIRIHIMIZ MUMKIN
#from avto_info_mod import avto_info, info_print

#avto1=avto_info('Gm','Malibu',"qora",'avtomat',2022,400000)
#info_print(avto1)

#from avto_info_mod import avto_info as ainfo, info_print as iprint
#avto1=ainfo('Gm','Malibu',"qora",'avtomat',2022,400000)
#iprint(avto1)

# mana bu(*) USUL BN MODULNI ICHIDAGI HAMMA FUNKSIYALARNI CHAQRIB OLISH MU MKIN
#from avto_info_mod import * # lekin bunday usul bn chaqirib olish tafsiya qilinmaydi
#avto1=avto_info('Gm','Malibu',"qora",'avtomat',2022,400000)
#info_print(avto1)

#import math

#x=16
#print(math.sqrt(x))  # BU YERDa sqrt KIRITILGAN SONNI KVADRAT ILDIZINI HISOBLAB BERADI
#print(math.pow(4,2)) # bu yerda (powor) sonning biror darajasi bu yerda 5 ni 3 darajasini hisoblaydi
#print(math.pi)
#print(math.log2(8))
#print(math.log10(100))

# RANDOM MODULI TASODIFIY SONLAR BILAN ISHLANGANDA ISGLATILADI
import random as r  # BU YERDA random DEGAN MODULNI OLIB KELIB UNI ICHIGA RENDINT() DEGAN FUNKSIYANI YUKLAYAPMIZ 

#randint() BU FUNKSIYA BILAN  ORALIQDAGI TASODIFIY SONNI CHIQARISH MUMKIN 
#son=r.randint(0,50) #MENDA TASODIFIY SON 57 CHIQDI
#print(son)



# CHOICE() FUNKSIYA BIROR BIR ROXATNI ICHIDAN 1 TA TASODIFIY QIYMATNI TANLAB OLADI
#ismlar=['ali','rano','karim','murod']
#ism=r.choice(ismlar)
#print(ism.title())
#print(r.choice(ism)) # Endi ismni ichidan ham bitta harf tanlab chiqaradi


#x=list(range(0,51,5))
#print(x)
#print(r.choice(x))

#YANA BIR FOYDALI FUNKSIYA BU FUNKSIYA ROYXATT ICHIDAGI QIYMATLARNI ARALSHTIRIB TASHLAYDI
#shuffle()
x=list(range(11))
print(x)
r.shuffle(x)
print(x)







