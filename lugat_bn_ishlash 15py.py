# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:45:39 2026

@author: ASUS
"""

# 15 Lugatlar bila ishlash
# .items() elememnti
#talaba_0={'ism':'murod olimov', 'yosh':26, 't_yil':2000}
#print(talaba_0.items()) # Items dan foydalanib lugatdagi kalit va qiymatni chiqiarib oldik

#for kalit,qiymat in talaba_0.items():
#    print(f"Kalit:{kalit}")
#    print(f"Qiymat:{qiymat}")

#telefonlar={
#    'ali':'samsung',
#    'nodir':"mini",
#    'shavkat':'15 pro',
#    'rasul':'G promax',
#    'olim':'galaxy'
#    }

#for k,q in telefonlar.items():
#    print(f'{k.title()} ning telefoni {q}') # Kodni chiroyliroq yozgani k KAlit q esa qiymati

# KEys() Lugatni ichidagi kalitlarni aniqlash uchu metod

#mahsulotlar={
#    'olma':10000,
#    'orik':20000,
##    'anjir':10000,
#    }

#print(mahsulotlar.keys()) # bu metod faqat mahsulotlarni kalit sozini chiqarib beradu yani keys sozlarni
# for tsiklidan foydalansak
#talaba_0={'ism':'murod olimov', 'yosh':26, 't_yil':2000}
#print('Do\'konimizdagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys(): # Bunda .keys() metodini ishlatmasa ham lugatdagi faqat keyslarni chiqarish mumkin
 #   print(mahsulot.title())

#print('Do\'konimizdagi mahsulotlar:')
#for mahsulot in mahsulotlar: # Bunda .keys() metodini ishlatmasa ham lugatdagi faqat keyslarni chiqarish mumkin
#    print(mahsulot.title())

#bozorlik=['ananas', 'anjir','avakado','apelsin','karam','orik','shaftoli']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f'{mahsulot.title()} {mahsulotlar[mahsulot]}  so\'m')

#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f'Ilrimos dokoningizga {buyum}  ham olib keling')

# Endi mana shu lugatni ketma ketlikda chiqarish uchun .sorted() metodini ishlatsak boladi
#print('Do\'konimizdagi mahsulotlar:')
#for mahsulot in sorted(mahsulotlar): # A harfidan boshlab tahlab chiqaradi. lekin royxatdagi tartib ozgarmaydi
#    print(mahsulot.title())

#LUgatni ichidagi elementlarni ozini chiqarish yani kalit emas qiymatni chiqarish uchun .values() metodidan ishlatiladi
#telefonlar={
#    'ali':'samsung',
#    'nodir':"mini",
#    'shavkat':'15 pro',
#    'rasul':'G promax',
#    'olim':'galaxy'
 #   }
#print(telefonlar.values()) # Bu usulda faqat qiymat chiqadi
#print('Foydalanuvchilar quydagi telefonlarni ishlatadi:')
#for tel in telefonlar.values():
 #   print(tel.title())

# Agar roxatda bir element qayta qayta bir necha marta chiqsa uni birlashtirib olish uchun .set() funksiyasidan foydalanib qisqa qilib olamiz
#telefonlar={
#    'ali':'samsung',
#    'nodir':"mini",
#    'shavkat':'15 pro',
#    'rasul':'G promax',
#    'olim':'galaxy',
#    'rano':'samsung',
#    'jasur':'mini',
#    'doston':'15 pro'}
#print('Foydalanuvchilar quyidagi telefonlarni ishlatadi:')
#for tel in set(telefonlar.values()):
#    print(tel.title())


toys={'ball','lamp', 'bear','car','tank','car'} # Setdagi malumotlar ozgarmas boladi va bir xil element bolsa tashlab yuborati







