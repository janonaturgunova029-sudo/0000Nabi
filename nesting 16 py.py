# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:53:31 2026

@author: ASUS
"""

# Bir narsani ichda boshqa narsa saqlash nesting deyiladi

#car0={
#      'model':'nexia 3',
#      'rang':'oq',
#      'yil':2018,
#      'narh':130000,
#      'kilometr':500000,
#      'karobka':'aftomat'
#      }
#car1={
#      'model':'lacetti',
#      'rang':'qora',
#      'yil':2015,
#      'narh':90000,
#      'km':89000,#
#    'karobka':'mexanika'
#      }
#car2={
#      'model':'gentra',
#    'rang':'qizil',
#      'yil':2019,
#      'narh':15000,
  #    'km':20000,
 #     'karobka':'mehanika'
#      }
#car=car2
#print(f'{car['model'].title()},'
#      f'{car['rang']} rang,'
#      f'{car['yil']}-yil, {car['narh']} $')



#cars=[car0,car1,car2]
#for car in cars:
#    print(f'{car['model'].title()},'
#         f'{car['rang']} rang,'
#         f'{car['yil']}-yil, {car['narh']} $')
 
##      f'{cars[2]['model']}')  


#malibus=[]
#for n in range(10):
#    new_car={
#        'model':'malibu',
#        'rang':None,
#        'yil':2020,
#        'narh':None,
#        'km':0,
#        'karobka':'avto'
#        }
#    malibus.append(new_car)
    
#for malibu in malibus:
#    print(malibu)

#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
 
#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
    
#for malibu in malibus[6:]:
#    malibu['rang']='qora'
#    malibu['karobka']='mexanika'
     
#for malibu in malibus:
#    print(malibu)


#for malibu in malibus:
#    if malibu['karobka']=='avto':
#       malibu['narh']=40000
#    else:
#        malibu['narh']=350000

# _- Bit kalit lugatni ichiga bir nechta qiymat berish uchun bunday usuldan foydalanamiz
dasturchilar={
    'ali':['phyton','c++'], # Bitta kalit ichida bir necha qiymatlar berishda shunday qavs ichida yozib olinadi
    'vali':['html','css','js'],
    'shokir':['php','sql'],
    'hasan':['phyton','php'],
    'nodir':['js','c#']
    }


#for ism, tillar in dasturchilar.items():
#    print(f'\n{ism.title()} quyidagi dasturlash tillarini biladi:')
#    for til in tillar:
#       print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f'\n{ism.title()} quyidagi dasturlash tillarini biladi:')
    for til in tillar:
       print(f'{til.upper()}', end='') # Oxirida end bilan tugashi sababi konsulda bosh joyni olib tashlaydi


























