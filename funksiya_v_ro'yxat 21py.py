# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:01:13 2026

@author: ASUS
"""

## FUNKSIYA VA ROYXAT
#def bahola(ismlar):
#    baholar={}
#    while ismlar:
#        ism=ismlar.pop()
#        baho=input(f'Talaba {ism.title()}ning bahosi:')
#        baholar[ism]=int(baho)
#    return baholar    

#talabalar=['nargiz','olima','hasan','husan']
#baholar=bahola(talabalar)
#print(baholar)



#def balla(ismlar):
#    ballar={ }
#    while ismlar:
 #       ism=ismlar.pop()
 #       bal=input(f'Student {ism.title()}ning bali:')
#        ballar[ism]=int(bal)
#    return ballar
   
#studentlar=['olim','anvar','diyor','matluba']
#ballar=balla(studentlar)
#print(ballar)


#FUNKSIYANING ASOSIY HUSUSIYATI BIZ LUGATGA MALUMOT UZATSAK FUNKSIYAGA ASL NUSHASI YUKLANADI
# Agar ikklasai ham tursin desak [:] belfgini ham qoshib ketamiz shunda talabalar degan royxatni nushasini dasturga uzatamiz


def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f'Talaba {ism.title()}ning bahosi:')
        baholar[ism]=int(baho)
    return baholar    

talabalar=['nargiz','olima','hasan','husan'] 
baholar=bahola(talabalar[:])
print('Talabalarga qoyilgan baholar')
print(baholar)












