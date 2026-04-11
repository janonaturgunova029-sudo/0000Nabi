# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:25:06 2026

@author: ASUS
"""

mevalar=['olma', 'ananas', 'kivi', 'malina']
sonlar=[1999, 3004, 546, -345, 9.678]
aralash_s=['alisher', 'tekin', 'warior', 7878,  6.798] #lugatda arash ham yyzosih mumkin

people=[]

#Lgatdagi elementlarni ozgartirish uchun ozgaruvchini olib kelib ozgartiramiz. 
# for exam   mevalar[3]='anor' shunda 3 chi raqamdagi lugat nomi ozgaradi


# Royxatga yanngi element qoshish uchun esa .Append() funksiyasidan foydalanamiz
# Append() funksiyasi doim royxat oxiriga yangi royxat nomini qoshib boradi

# Agar royxatga aynan bir joyiga element qoshishni istasak  .INsert() funksiyasidan
# foydalanamiz. f ex. mevalar.insert(0, 'anor')


# - Endi esa royxatdagi malum elenmentni ochirish uchun "Del" funksiyasidan
# foydalanamiz. f ex. del mevalar[2] indeks nomini kiritib ochiramizflavors.insert(0,'binafsha')


# - Agar royxatdan elementni indeksini bilmasa unda ."remove" metodidan foydalanib
# aynan bir elementni ochirib tashlash imkoni bor. for ex. gullar.remove("lola')


# - Remove metodi royxatdagi birinchi elementni ozin ochoradi. agarroyxatda 
# bir element ikki marta kelsayu ochirmoqchi bolsa unda 'remove' metodi
# royxat boshdagi elementni ozini ochiradi

gullar=['tirnoqgul', 'nargiz', 'safsargul', 'binafsha', 'nargiz']

# - Range funksiyasi malum bir oraliqdagi sonlarni qaytaradi,
# yani oraliqdagi sonlarni chiqarib beradi f.ex range(0,10)  
# bu range sonidan hosil bolgan sonlarni royxatga otqazish uchun 'list'
#funksiyasini ishlatamiz.  list(range(0,10))


#royxatga  toq sonlarni chiqarish uchun 2 qadamdan tahslab ketiladi' misol toq sonalr=list(range(1,20,2))
# -Juft sonlarga ham 2 qadam tahslanadi 0 dan boshlab
#toq_sonlar=list(range(1, 40, 2))
#print(toq_sonlar)

#juft_sonlar=list(range(0, 61,2))
#print(juft_sonlar) # yagona farqi juft sonlar '0' dan boshlanadi


# Sonlar ichida maximum qiymatni topish ham mumkin buning uchun 'max' funksiyasidan foydalanamiz
# misol 'max_qiymat=max(toq_sonlar)


# Minumum qiymatni yani kichik qiymatni topish uchun 'min' funksiyasidan foydalanamiz
# misol "min(sonlar)" deb 5f tugmasi bosiladi va consulda minimum sonlar chiqib keladi


# Sonlarni umumiy yigindisini topish uchun "sum" funksiyasi ishalatiladi
# - misol "sum(narhlar)"

yillar=[1888, 1675, 20000, 8743, 12, 99763,10001]
#eng_keksa_yil=max(yillar)
#jami_yashalgan_yillar=sum(yillar)
#print('meni dugonam shuncha yilmiyyamni egovladi',eng_oz_yil,"yil", 'lekin men unga shuncha yil bardosh bera oldim',
#      eng_keksa_yil, 'lekin hisoblab korsam ancha bardoshli yil qizman ekan jami:', jami_yashalgan_yillar)

qisqa=min(yillar)
uzun=max(yillar)
jami=sum(yillar)
print('eng qisqa yil', qisqa, 'yil','eng uzn yil', uzun, 'yil', "umumiy yillar", jami, 'yil')


# -RoyxATDAN MALUM BIR QISMINI SUGURIB CHIQARIB OLISH UCHUN ROYXAT NOMI
# [0:8] GACHA KORINISHIDA ORTAGA : NUHTA BERILADI

# endi esa listdan biron lugatni nusha olish uchun 
# bunday qilinadi. - mening gullarim=gullar