# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:45:04 2026

@author: ASUS
"""
# AMALIYOT
#1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
#2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

# JAVOBLAR
## GitHub
#def son_kopaytmasi(*sonlar):
#    kopaytma=1
#    for son in sonlar:
#        kopaytma*=son
#    return kopaytma
    
#print(son_kopaytmasi(2,5,5,6))
#print(son_kopaytmasi(11.34,98))
        

def talaba_m(ismi, familiyasi, **malumot):
    malumot['ismi']=ismi
    malumot['familiyasi']=familiyasi
    return malumot

talaba1=talaba_m('odil','alimov',yoshi=12,kasb='talaba')
talaba2=talaba_m('komil','ganiyev',yoshi=35, kasb='oqituvchi')
talabalar=talaba1 /: talaba2
print(talabalar)



























