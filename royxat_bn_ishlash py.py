# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:52:42 2026

@author: ASUS
"""

#  Lugatni alifbo tartibidia tahlab berish funksiyasi "Sort()" dan ishlatiladi'
# f ex gullar.sort()


# Agarda endi buni alfabit teskarisigaolib kelmoqchi bolsak revorse elementidan
# foydalanamiz.  f ex. gullar.sort(reverse=True)


#  -Endi esa royxatni ichiga tegmagan holatda consuldan elementni alifbo
# tarkibida teskarisiga tartiblab chiqarish uchun "Sorted" funksiyasidan foydalanamiz.
# f exam print(sorted(gullar))

#ranglar=['qizil', 'sariq', 'oq','pushti', 'moviy']


#sonlar=[99, 1,13, 1499, 0.19, -1.99]


# -Endi esa royxatni teskarisiga aylantirib qoyish uchun '.reverse()' metodidan
# foydalanamiz. f ex. cars.reverse()

#Royxatni uzunligini olchash uchun yani royxatda nechta element borligini aniqlash
#uchun 'len' funksiyasidan foydalanamiz

#xashoratlar=['qong\'iz','chigirtka','suvarak','honqizi','sichqon']

#- Agar royxatni ichidan nusha olsak ham ikklasi bir xil royxat bolib qolmasligi uchun kodimizni quydagi usulda yozishimiz kerak
# mening_xashoratlarim=xashoratlar[:] qavs ichidagi ikki nuxta royxatdagi barcha elementlarni chiqarib beradi
#baliqlar=('ilonbaliq','sazan','oltin baliq')# Tuple fayli bu ozgarmas fayl hisobandi unga qoshib ham ayrib ham bolmaydi/
# -Royxatni qaytarib tyuple ozgarmasga otqazib qoysa ham boladi.

#davlatlar=['aqsh', 'kanada','us','malaysia', 'singapur']
#davlatlar.sorted()
#Agar 'tyuple' ni ozgartirmoqchi bolsak unda avval uni listga ozgartirib olishimimz kerak
#misol baliqlar=list(baliqlar) shunda bu lugattimi tyuple dan listga otadi va undan nusha kochirib ishlatishimiz mumkin
# ishlatib bolgandan song esa uni qayta baliqlar=tyuple(baliqlar) deb qayta tyuple ga otqazib qoyamiz
 
#juft_sonlar=list(range(0,20,2))
#toq_sonlar=list(range(1,30,2))
#print('juft sonlar:', juft_sonlar)
#print('Toq sonlar:', toq_sonlar) 

#shakllar=['yumaloq', 'uchburchak','oval', 'tortburchak','aylana']
#print(shakllar)
#print(sorted(shakllar))
#print(shakllar.sort())

mevalar=['gilos','olma','kivi','tarvuz']
#mevalar.sort()
#print(mevalar)
#mevalar.sort(reverse=True)
#print(mevalar)
#mevalar.sorted()
#print(sorted(mevalar))
#print(sorted(mevalar))
mevalar=['gilos','olma','kivi','tarvuz']
print(sorted(mevalar,reverse=True))

yosh=[99,18,8,45,31,65]
#yosh.sort()
#print(yosh)
#print(sorted(yosh, reverse=True))
yosh.reverse()
print(yosh)
oila=['amma','toga','hola','kenayi','aka']
oila.reverse()
#print(oila)
print('Elementlar soni:', len(oila))


sonlar=list(range(0,81))
print(sonlar)

yillar=[87,13,43,65,77,81,15]
kam_yil=min(yillar)
kop_yil=max(yillar)
umumiy_yil=sum(yillar)
print('eng kop boks bilan shugillangan oquvchi yili:',kop_yil, 'eng kam shugillangan oquvchi:',
      kam_yil, 'umumiy shugillanilgan yillar', umumiy_yil)

#kolalar=['koka kola','pepsi','fanta', 'tems',"zero kola"]
#mening_kolam=kolalar[0:4]
#print(mening_kolam)
#print(kolalar[0:3])
#print(kolalar[2:])
#print(kolalar[:4])
 
davlatlar=['aqsh','kaliforniya','malaysia','sidney']
#davlatlar.insert(0,'angilya')
#print(davlatlar)
#davlatlar.insert(1,'olmoniya')
#print(davlatlar)
#davlatlar.insert(2,"Switzerlandiya") 
#print(davlatlar)
#davlatlar.insert(3,'tayland')
#print(davlatlar)
#davlatlar.insert(4,'shatlandiya')
#print(davlatlar) 
davlatlar=["kanada",'angilya','yevropa','yaponiya']     
sayohat_d=davlatlar
print(sayohat_d)
sayohat_d.remove('kanada')
print(sayohat_d)
sayohat_d.remove('yevropa')
print(sayohat_d)