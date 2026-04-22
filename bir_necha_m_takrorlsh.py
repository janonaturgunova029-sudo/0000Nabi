# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:44:18 2026

@author: ASUS
"""

# 11 dars if/elif/else bir necha marta takrorlash

#son=-56
#if son<0:
 #   print('manfiy son')
#else:
 #   print('musbat son')

#yosh=int(input('YOshinigiz nechida?'))
#if yosh<=2:
#   narh=0 # print('Sizga kirish bepul')
#elif yosh<=8:
#    narh=5000 #print('Sizga kirish 500 som')
#else:
 #  narh=10000# print("Sizga kirish 1000 som")
#print(f"sizga kirish{narh} so\'m")


#kun=input('Buvun nima kun?\n>>')
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('Bugun dam olish kuni')
#else:
#    print('Bugun 출군합니다')

#kun=input('Bugun nima kun?')
#harorat=float(input('havo haroarati qanday?'))

#if kun.lower()=='shanba' and harorat>=30:
#     print('Chomilgani kettik')
#elif kun.lower()=='shanba' and harorat<30:
#     print('Bugun dam ol!')
 
# Bollean malumot turi

#narh= 10000
#choy=True
#salat=True

#if choy and salat:
#    narh= narh+20000
#elif choy or salat:
#    narh= narh+5000
    
#print(f"Jami {narh} so'm")    

#uzunlik= 30
#kenglik=True
#balandlik=False

#if kenglik and balandlik:
#    uzunlik= uzunlik+20
#elif kenglik or balandlik:
 #   uzunlik= uzunlik+40
    
#print(f'Uzunlikni umumiy olchami {uzunlik} km')

# IN aperateri biron narsani royxat ichidA BPORMI yoqmi tekshiraadi

#menu=['osh','norin','honim','chuchvara']
# 'manti' in menu
#ovqat=input('Nima ovqat yeysiz?')
#if ovqat.lower() not in menu:
#   print('Afsuski bizda bu ovqat hozir yoq')
#else:
#     print('buyurtma qabul qilindi')
# NOT IN aperatiri yordamida malumot yoqmi deb soras boladi


menu=['osh','norin','honim','chuchvara','dimlama','somsa', 'shorva']
buyurtmalar=['shorva','somsa','dimlama','makaron']

for taom in buyurtmalar:
  if taom in menu:
    print(f'Menuda {taom} bor')
  else:
     print(f"Kechirasisiz , menuda {taom} yoq")







