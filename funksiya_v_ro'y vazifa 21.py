# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:10:52 2026

@author: ASUS
"""


#def katta_harf(matnlar):
# for i in range(len(matnlar)):
#   matnlar[i]=matnlar[i].title
      
#ismlar=['ali','asror','nodir','sharif']
#katta_harf(ismlar)
#print(ismlar)
    

#def katta_harf(matnlar):
#    for m in range(len(matnlar)):
#        matnlar[m]=matnlar[m].title()
        
#sozlar=['olma','urish','yurak','muz']
#katta_harf(sozlar)
#print(sozlar)

#def katta_harf(matnlar):
#    matnlar=matnlar[:]
 #   for o in range(len(matnlar)):
#        matnlar[o]=matnlar[o].upper()
#    return matnlar 
    
#olimlar=['isb sino','bobur','beruniy','buxoriy']
#yangi_ismlar=katta_harf(olimlar)
##print(yangi_ismlar)

talaba=['ali','shuhrat','olim','mansur']

def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f'Talaba {ism.title()} ning bahosi')
        baholar[ism]=baho
    return baholar
        
baholar=bahola(talaba)
print(talaba)
print(baholar)



















