# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:14:27 2026

@author: ASUS
"""
# inkopulyatsiya bror funksiyasini xususiyatini yashirish
from uuid import uuid4
class Avto:
    """Avtomobil classi"""
    __num_avto=0
    """AVtoga tegishli funksiya"""
    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomabilning hususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km ##Kapsulyatsiya yashirin xususiyati tahsqqaridan murojat qilib bolmaydi
        self.__id=uuid4()
        Avto.num_avto+=1
        
    def get_km(self):
        return self.__km     
    
    def get_id(self):
        return self.__id ##Bundan qilishdan yashirishdan maqsad bazida foydalanuvchini bu codni ozgartirisini hohlamaslik uchun yashirin qilinadi

    def add_km(self,km):
        """Mashinaning kmga yana km qoshadigan method"""
        if km>=0:
            self.__km+=km
        else:
            print("Moshinani km kamaytirib bolmaydi") #9




















