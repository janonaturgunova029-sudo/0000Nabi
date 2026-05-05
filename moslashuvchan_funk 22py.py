# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:24:12 2026

@author: ASUS
"""

# OZGARUVCHAN FUNKSIYALAR YARATISHNI ORGANISH
# *args USULI BILAN FUNKSIYAGA ISTAGANCHA PARAMETR,ARGUMENT KIRITISH QOSHISH MUMKIN

#def summa(*sonlar):
#    """Kiritlgan sonlar yigindisini hisoblaydigan funksiya"""
#    yigindisi=0
#    for son in sonlar:
#        yigindisi+=son
#    return yigindisi

#print(summa(1,2))
#print(summa(1,2,3,4))


#def summa(*sonlar):
#    return sum(sonlar)
 

#print(summa(1,2))
#print(summa(1,2,3,4))
#print(summa(5,6,7,8,9))


#Funksiya chaqirilganda qavs ichida qiymat berishning sababi shundaki, funksiya tashqaridan ma’lumot qabul qilishi uchun parametrlar kerak.

#📌 Batafsil:

#Funksiya — bu biror vazifani bajaradigan kod bo‘lagi. Lekin u ko‘pincha umumiy yoziladi, ya’ni aniq sonlar yoki matnlar bilan emas, balki parametrlar bilan ishlaydi.

#Qavs ichidagi qiymatlar (argumentlar) — funksiyaga tashqaridan beriladigan ma’lumotlar. Funksiya shu ma’lumotlar ustida ishlaydi.



#Agar qavs ichida qiymat bermasak, funksiya hech qanday ma’lumot
# olmaydi va natija chiqmaydi. Shuning uchun qavs ichida
# qiymat berish — funksiyaga ishlash uchun “xomashyo” berish demakdir.

# PARAMETRSIZ FUNKSIYA
#def salom_ber():
#    print("Salom, dunyo!")

#salom_ber()

# PARAMETRLI FUNKSIYA TASHQARIDAN QIYMAT QABUL QILIB NATIJANI CHIQARIB BERADI
#def salom_ber(ism):
#    print(f"Salom, {ism}!")

#salom_ber("Ali")
#salom_ber("Vali")



#Qayta foydalanish (reusability)

#Oddiy kodni bir marta yozib ishlatamiz, keyin yana kerak bo‘lsa qayta yozishimiz kerak.

#Funksiya esa bir marta yoziladi, keyin istalgan joyda chaqirib ishlatish mumkin.


#Tartib va tozaligi (organization)

#Funksiyalar kodni bo‘laklarga ajratadi. Har bir funksiya bitta vazifani bajaradi.

#Bu kodni o‘qishni va tushunishni osonlashtiradi.

#Oddiy kod — bir martalik ishlatish uchun.
#Funksiya — ko‘p marta ishlatish, tartib va moslashuvchanlik uchun.

#def summa(x,y,*sonlar):
#    return x+y-sum(sonlar)

#print(summa(1,2))
#print(summa(98,123,45,67))
#print(summa(32,14,56,76,87,1))
#print(summa(4))

#  KWARGS (KEY WORDS)-ARGUMENTS

#def avto_info(kompaniya,madel,**malumotlar):
#    malumotlar['kompaniya']=kompaniya
#    malumotlar['madel']=madel
#    return malumotlar

#avto1=avto_info('GM','malibu',rang='qora',yil=2019)
#

#return funksiyada juda muhim vazifa bajaradi: u funksiya ichida hisoblangan natijani tashqariga chiqaradi.

#📌 Agar return bo‘lmasa, funksiya chaqirilganda faqat ichidagi kod bajariladi, lekin hech qanday qiymat qaytmaydi. Python’da bunday holatda funksiya None qaytaradi.
def sport_tur(nomi,odam_soni, **malumotlar):
    malumotlar['nomi']=nomi
    malumotlar['odam soni']=odam_soni
    return malumotlar

sport1=sport_tur('Futbol','7 kishi', varata='1 kishi himoya',vaqti='95 min')
sport2=sport_tur('Shaxmat','2 kishi oynaydi',oyin_sharti='mot qilgan yutadi',toshlar=16)
























