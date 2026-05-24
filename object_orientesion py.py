# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:10:58 2026

@author: ASUS
"""
# 28 DARS Object orientetion darsi

# Chiziqli tartibli dasturlash 
#Afzalliklari:
#    dasturlahni organish qulay
#    sodda va tushinarli kod
#    dastur aloritmini kuzatish odon
#    dastur hotirada kamroq joy egallaydi
    
    
##         murakkab dasturlarni chiziqli usuldz yozish qiyin
#         Bir dastur uchun yozilgan kodda boshqa dasturda qayta foydalanib bolmaydi
#         Dastur ichidagi malumotlar (ozgaruvchilar) barcha funksiyalar ucun ochiq
#        ZAMONAVIY DASTURLAR CHIZIQLI EMAS


#| Afzallik | Izoh |
#| --- | --- |
#| **Modullilik** | Kodni bo‘laklarga ajratish oson, boshqarish qulay. |
#| **Qayta foydalanish** | Klasslar va metodlar boshqa loyihalarda ham ishlatilishi mumkin. |
#| **Kengaytirish** | Yangi funksiyalar qo‘shish oson, mavjud kodni buzmaydi. |
#| **Xatolarni kamaytirish** | Enkapsulyatsiya orqali noto‘g‘ri foydalanishdan himoya qiladi. |
#| **Real dunyo modeliga yaqinlik** | Obyektlar real hayotdagi narsalarni ifodalaydi (mashina, odam, kitob). |


#🌍 Mashhur OOP tillari
#Java – keng tarqalgan, ayniqsa korporativ dasturlarda.

#Python – oddiy sintaksis, o‘rganish oson.

#C++ – kuchli, tezkor, lekin murakkab.

#C# – Microsoft ekotizimida keng qo‘llaniladi.

#JavaScript (ES6) – veb dasturlashda obyektga yo‘naltirilgan imkoniyatlar mavjud.


#📌 Xulosa
#Object-oriented dasturlash sizga murakkab 
#dasturlarni tartibli va boshqariladigan shaklda yozish imkonini beradi.
# Agar siz yangi boshlayotgan bo‘lsangiz, 
# klass va obyekt tushunchasidan boshlash eng to‘g‘ri yo‘l bo‘ladi.
# Keyin enkapsulyatsiya, meros olish va polimorfizmni o‘rganib, real loyihalarda qo‘llashni mashq qilishingiz mumkin.

#x=10
#print(x)

class Talaba:
    def __init__(self,ism,familiya,t_yili): # self"_
        self.ism=ism
        self.familiya=familiya
        self.tyil=t_yili
        
    def get_name(self):   
        return self.ism
    
    def get_age(self,yil):
        return yil-self.tyil
    def get_last_name(self):
        return self.familiya
        
    def tanishtir(self):
        return f'Ismim {self.ism} {self.familiya}, tug\'ilgan yilim {self.tyil}'
        

talaba1=Talaba("Olim",'Olimov',2000)
talaba2=Talaba('Nodir','Komilov',1998)














































