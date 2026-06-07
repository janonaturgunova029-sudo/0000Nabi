# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:02:21 2026

@author
"""


class Shaxs: #Bu yerda Shaxs super() klass boladi
    """Shaxlar haqida malumot"""
    def __init__(self,ism,familiya,pasport,tyil):
        """Shaxning hususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.pasport=pasport
        self.tyil=tyil
        
    def get_info(self):
        """Shaxs haqida malumot"""
        info=f'{self.ism} {self.familiya}.'
        info+=f'Pasport: {self.pasport}, {self.tyil} yilda tugilgan'
        return info
    def get_age(self,yil):
        """Shaxsning yoshini aytuvchi metod"""
        return yil-self.tyil
        
#Endi shu klassdan yangi klas yaratish
class Talaba(Shaxs): #Talaba voris klas
    """Talaba klasi"""
    def __init__(self,ism,familiya,pasport,tyil, idraqam, manzil):# Bu yerda xususiyatni qisqaroq qilish uchun yangi klass yaratamiz
        """Talaabaning hususiyati""" 
        super().__init__(ism,familiya,pasport,tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil

    def get_id(self):
        """TAlabaning id raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning oqish bosqichi"""
        return self.bosqich
   ##Polimarfizm

    def get_info(self): ##Polimarfizm BUnda voris kalssda yaratilgan metodlar bilan birga chaqiriliar ekan
        """Talaba haqida malumot"""
        info = f'{self.ism} {self.familiya}.'
        info+=f"{self.get_bosqich()}-bosqich. ID raqami {self.get_id()}"
        return info


class Manzil:
    """Manzil saqalash uchun klass"""
    def __init__(self, uy,kocha,tuman,viloyat):
        """Manzil xuxuxxiyatlari"""
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
        
   
    def get_manzil(self):
        """MAnzilni korish"""
        manzil=f'{self.viloyat} viloyati, {self.tuman} tumani,'
        manzil+=f"{self.kocha} kochasi, {self.uy} uy"
        return manzil

talaba1_manzil=Manzil(12, "olmazor","Bogbon", 'Xorazm')
talaba1=Talaba('Alijon', 'Mamajonov', 'FS9177363',2000,'No22222',talaba1_manzil)


































