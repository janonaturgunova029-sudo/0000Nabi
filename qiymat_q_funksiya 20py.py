# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:08:09 2026

@author: ASUS
"""
# VAZIFA 20 

#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#    """Toliq isma qaytaruvchi funksiya"""
#    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
 #       toliq_ism = f"{ism} {otasining_ismi} {familiya}"
 #   else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()

#talaba1=toliq_ism_yasa('olim','komilov')
##print(f"Bugun darsga kelgan oquvchilar {talaba1} va {talaba2}")


#def oraliq(min,max):
#    sonlar = [] # bo'sh ro'yxat
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar

#print(oraliq(0,11))
#print(oraliq(10,31))


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1=avto_info('Gm','Nexia',"OQ",'Avto',2019, 38000)
avto2=avto_info('Toyota','Kobalt','Qizil','Mexanik',2022)
avtolar=[avto1,avto2]
print('Online bzorgdagi mavjud mashinalar')
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Nomalum"
    print(f'{avto['rang']} {avto['model']}. Narhi:{narh}')



























