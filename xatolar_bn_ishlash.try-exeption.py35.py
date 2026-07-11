# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:10:42 2026

@author: ASUS
"""

# Hatolar bilan ishlash try-exept 35 dars


#yosh=input("Yoshingizni kiriting: ")
#try:
#   yosh=int(yosh)
#   print(f"Siz {2026-yosh} yilda tugilgansiz")
#except ValueError:
#    print("Butun son kiriting iltimos!")
    
    #Zero divitsion error
#x,y=5,10
#try: 
#    y/(x-5)    
#except ZeroDivisionError:
#    print("0 ga bolib bolmaydi")

mevalar=['olma','anor','orik','shaftoli']
try:
   print(mevalar[3].title())
except IndexError:
    print(f"Royxatda {len(mevalar)} ta meva bor xolos")     



































