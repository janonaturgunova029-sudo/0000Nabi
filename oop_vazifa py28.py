# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:30:43 2026

@author: ASUS
"""


#Demak, Pythondagi har qanday o'zgaruvchi, funksiya va boshqa elementlar aslida obyektlar ekan.

# METODLAR

#Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bu funksiyalar obyekt ichida yashirin bo'ladi, va biz ularga nuqta va funksiya nomi orqali murojat qilishimiz mumkin. Bunday funksiyalar shu klass (yoki obyektga) tegishli **metodlar** deyiladi.

#Biz ba'zi metodlar bilan avvalgi darslarimizda tanishdik. Bir klassga tegishli metodlar, boshqa klassdagi obyketlar uchun mavjud bo'lmasligi tabiiy. Misol uchun matnlar uchun mavjud metodlarni, butun yoki o'nli sonlarga qo'llab bo'lmaydi.


# `pass` OPERATORI

#Pythonda hech qanday vazifani bajarmaydigan `pass` operatori mavjud. Bu operatordan bo'sh metodlar yaratishda foydalanish mumkin. Misol uchun siz klassingiz uchun muhim metodlarni bilasiz, lekin metod badani hali tayyor emas. Agar metod badanini bo'sh qoldirsangiz, Python `IndentationError` xatosini qaytaradi. Shunday xolatlarda, funksiya badaniga `pass` operatorini qo'yib ketishimiz mumkin:


#class User:
#    def __int__(self,name,username,email):
#        self.name = name
 #       self.uname = username
#        self.mail = email
    
#    def describe():
#        pass
    
#    def get_email():
#        pass


class User:
    def __init__(self, ism,email,manzil):
        self.ism=ism
        self.email=email
        self.tjoy=manzil
     
    def get_info(self):
        return f'Foydalanuvchi: {self.ism}, email manzilim {self.email}; manzili {self.tjoy}'

user1=User('Tursun','thydgg454@gmail.com','yongbongon 121 ho')
user2=User('Cas21','memona091@email.com', 'Milliy bog 43 uy')        
        
    











