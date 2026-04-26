# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:11:32 2026

@author: ASUS
"""

#telefonlar={
#    'ali':'samsung',
#    'nodir':"mini",
#    'shavkat':'15 pro',
#    'rasul':'G promax',
#    'olim':'galaxy',
#    'rano':'samsung',
#    'jasur':'mini',
 #   'doston':'15 pro'
#    }

#print(telefonlar.items())
#for k,q in telefonlar.items():
#    print(f'kalit:{k}')
#    print(f'Qiymat {q}')

#for k,q in telefonlar.items():
#  print(f'{k.title()} ning telefoni {q}')

#print(telefonlar.keys())


#mahsulotlar={
#    'olma':10000,
#    'orik':20000,
#    'anjir':10000,
#    }
#print("Dokonimizdagi mahsulotlar")
#for mahsulot in mahsulotlar:
#    if mahsulot in sorted(mahsulotlar):
#        print(mahsulot.title())
        
#print(telefonlar.values())       
#print('Foydalanuvchilar quyidagi telefonlarni ishlatadi:')
#for tel in telefonlar.values():
#    print(tel)

#print('Foydalanuvchilar quyidagi telefonlarni ishlatadi:')
#for tel in set(telefonlar.keys()):
#    print(tel.title())

# -VAZIFALAR
#py_lugat={
#    'set':'bir xilni tashlash',
#    'values':'qiymatlarni ozini chiqarish',
#    'keys':'kalit sozlarni chiqarish',
#    'items()':'lugatni chiqarish'
 #   }

#print(py_lugat.items())
#print(py_lugat.values())
#print(py_lugat.keys())

#davlat_cap={
#    'fransiya':'paris',
#    'thailand':'bankok',
#    'yaponiya':'tokio',
#    'germaniya':'berlin',
#    'kanada':'ottawa'
#    }
#for cap in sorted(davlat_cap):
#    if cap in davlat_cap.keys():
#        print(cap.title())

#for cap in davlat_cap:
#  if cap in sorted(davlat_cap.values()):
#    print(cap.title)

#davlatlar={
#    'fransiya':'paris',
#    'thailand':'bankok',
#    'yaponiya':'tokio',
#    'germaniya':'berlin',
#    'kanada':'ottawa'
#    }


#davlat=input('Istalgan davlatni kiriting va poytaxtni biling:')
#poytaxt=davlat_cap.get(davlat)
#if poytaxt==None:
#    print('Bizda bunday malumot yo\'q')      
#else:
 #   print(f"{davlat.upper()} ning poytaxti {poytaxt.title()} shahri")
      
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print('3 taom buyurtma qiling:')
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f'{n+1}-taom:').lower())
for buyurtma in buyurtmalar:     
    if buyurtma in menu:
        print(f'{buyurtma.title} narhi {menu[buyurtma]} som ')
    else:
         print(f'Bizda {buyurtma} taom yoq')     










