# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:47:57 2026

@author: Boglarda gullar ustida shabnam durlarini terish aynan bunday gozal kunga mos
"""
# 29 Obyektlar bilan ishlash

class Talaba:
    def __init__(self,ism,familiya,t_yili): # self"_ hamam hususiyatlarni parametrha kiritishh shart emas
        self.ism=ism
        self.familiya=familiya
        self.tyil=t_yili
        self.bosqich=1 # Bu bosqich degan funksiyani qiymatga qoshmaymiz

    def tanishtir(self):
        return f'Ismim {self.ism} {self.familiya} tug\'ilgan yilim {self.tyil} bosqichim {self.bosqich} da'
    
    def get_name(self):
        "Talabaning ismini qaytaruvchi funksiya"
        return self.ism
    
    def get_last_name(self):
        "TAlabaning familiyasini qaytaruvchi funsiya xususiyat"
        return self.familiya
    
    def set_bosqich(self, yangi_bosqich):
        """Talabaning bosqichini yangi kiritlgan bosqichga ozgartirish"""
        self.bosqich=yangi_bosqich
        
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga kotaradi"""
        self.bosqich+=1
        
class Fan():
    """Fan nomli classs"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
        
    def add_student(self,talaba):
        """FAnga talabalar qoshadi"""
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida malumot"""
        return [talaba.tanishtir() for talaba in self.talabalar]
    
    def get_stuens_num(self):
        """Fanga yozilgan talabar soni"""
        return self.talabalar_soni

    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith('__')]
    
matematika=Fan('Algebra')
talaba1=Talaba('Mansur','Hakimov',1999)
talaba2=Talaba('Olim','Salimov',2003)
talaba3=Talaba('Akrom','Sadullayev',1997)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)





























