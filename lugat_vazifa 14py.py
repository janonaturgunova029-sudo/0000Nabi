# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:30:47 2026

@author: ASUS
"""

#otam={'ism':'E','t_yil':1971, 'shahri':'Andijon','manzili':'qoshtepa'}
#print(f'Otamning ismi {otam['ism']}\
#      {otam['t_yil']} yilda\
#     {otam['shahri']} viloyati\
#     {otam['manzili']} qishlog\'ida tugilgan')
    
#taomlar={
#    'dadam':'shirguruch',
#         'onam':'qozonkabob',
#         'singlim':'osh',
#         'ukam':'lagmon'
#         }
#print(f'Dadamning sevimli taomi {taomlar['dadam']}\
#     odamning sevimli taomi {taomlar['onam']}\
#    ukamning sevimli taomi {taomlar['ukam']}')

p_lugat={'int':'onlik son','float':'butun son','str':'matn','if':'yoki', 'else':'bolmasa'}
#print(f'Int bu py tilida {p_lugat['int'].upper()} degan manoda ishlatiladi')
#print(f'Float metodi sonlarni\
#     {p_lugat['float'].title()}\
 #    songa o\'tqazadi')
#print(f'Pytonda matnlar bilan ishlaganda str metdoi bor bu matnlarni\
#      {p_lugat['str']} korinishiga otqazib beradi')
#print(p_lugat['if'])


p_lugat={
    'int':'onlik son',
    'float':'butun son',
    'str':'matn',
    'if':'yoki',
    'else':'bolmasa'
    }
#print(p_lugat['tuple'])
kalit=input("istalgan sozni kiriting:").lower()
print(p_lugat.get(kalit, 'Bunday soz mavjud emas'))






#kalit=input("Kalit sozni kiriting:").lower()
#tarjima=p_lugat.get(kalit)
#if tarjima==None:
#    print("Bunday soz mavjud emas")
#else:
#    print(f'{kalit.title()} sozi {tarjima} deb tarjima qilnadi')    
    
    
  

















