# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:27:18 2026

@author: ASUS
"""
##Dunder methodlar tagida ikki chiziq bilan yoziladigan methodlar
class Avto:
    """Avtomobil classi"""
    __num_avto=0
    """AVtoga tegishli funksiya"""
    def __init__(self, make, model, rang, yil, narh,km):
        """Avtomabilning hususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km ##Kapsulyatsiya yashirin xususiyati tahsqqaridan murojat qilib bolmaydi
        Avto.__num_avto+=1

#    def __str__(self): ##Bu consuldA MALUMOTNI TOIQROQ QAYTARISH UCHUN
#        return f"Avto:{self.make} {self.model}"
    
    def __repr__(self):
        return f"Avto:{self.make} {self.model}" #Bu ham str bilan bit xil
    
    def __eq__(self,y):
        return self.narh==y.narh
    
    def __lt__(self,y):
        return self.narh<=y.narh
    
    
        
        
avto1=Avto("Gm",'Malibu','qora',2003,4000,300)
avto2=Avto('Hyundai', 'Bmw',' qizil', 2019, 3000, 300)
print(avto1)





















