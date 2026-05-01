# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:21:57 2026

@author: ASUS
"""
# !9 dars Funksiya BIR NECHA QATOR KODLAR YIGINDISI FUNKSIYA DEYILADI
# ozimiz qanday qulib print, range, type kabi funksiyalarni yaratishnni organamiz

# 'DEF' FUNKSIYA YARATISH APERATORI KALTILI
#def salom_ber():
#    """Ssalom beruvchi funksiya"""
#    print("Assalomu alaykum")
    
#salom_ber() 


#def ism_sora():
#    """Ism sorovchi funksiya"""
#    print("Ismingiz nima?")
    
#ism_sora()

#(DOCSTRING) FUNKSIYA HAQIDA MALUMOT. FUNKSIYA YARATGANDA MALUMOTNI TUSHINARLI QILIB YOZISH KERAK

#def salom_ber(ism):
#    """Foydalanuvchi ismini qabul qilib,
#    salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, Hurmatli {ism.title()}")

#salom_ber('hasan')
#salom_ber('olim')

#def toliq_ism(ism,familiya): #FUNKSIYAGA BIR NECHA QIYMAT BERGANDA qiymatga iki yoki uchta argument kiritiladi
#    """Foydalanuvchining ism, familiyasini jamlab chiquvchi funksiya"""
#    print(f"Foydalanuvchining ismi: {ism.title()}\n"
#          f"Foydalanuvchining familiyasi: {familiya.title()}")

#toliq_ism('olim','hakimov')
#toliq_ism('hakimov','olim')

def yosh_hisobla(ism, tugilgan_yil ):
   """Foydalanuvchising yoshini hisoblaydigan dastur"""
   print(f'{ism.title()} {2026-tugilgan_yil} yoshda')

#yosh_hisobla('olim', 1999)
#yosh_hisobla(1999,'olim') # HATO

#yosh_hisobla(tugilgan_yil=1999, ism='nodir') # HATOLIKNI OLDINI OLISH UCHUN PARAMETR NOMI BILAN YOZIB KETILADI


def yosh_hisobla(tugilgan_yil, joriy_yil=2026):
    """Foydalanuvchi tug'yilgan yildan uning yoshini hisoblaydi"""
    print(f'Siz {joriy_yil-tugilgan_yil} yoshdasiz')
    
#yosh_hisobla(1999,2026)
yosh_hisobla(1999)






























