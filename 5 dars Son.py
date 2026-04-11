# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:02:51 2026

@author: ASUS
"""
#bugungi darsozgaruvchi ichiga sonlarni saqlash
#a=20 integer- butun son 
#b=5.8 float-suzuvchi onlik nuqtali son

#temp=36.6 #ozgaruvchilarni nomini aniqlaah uchun Type sunksysidan foydalanish mm

#a=90
#print(type(a))

#print(type(temp))
 
#aholi_soni=4_367_987_453 #bu yozilga pastki chiziqlar raqamga tasiri yoq
#print("Dunyo boyicha aholi soni", aholi_soni) #ozgaruvchi pastki chiziq bilan yozilishi
#bu umumiy qoida


# Shu bilan birga bir necha ozgaruvchilarga bir nechs sonlarnui ham yuklash mn
#x,v,l= 9, 0.3, -92

a=43
b=7.7
c=a*b  # bu yerda c butun son bolsada hotirada onlik son bolib saqlanadi milos 
#javobi 110.0 bolsa nolni tashlab yubormasdan oshanday hotiraga joylaydi

d=200/5 # bu yerda ham aslida javob 50 boladi lekin kampyuter hotiraga 50.0 deb saqlaydi
 # endi buni butun songa otqazish uchu ikkkita // bolish belgisi ishlatamiz
 
d=300//6 #ana endi buni javobi 50 bolib chiqadi 50.0 emas
  

# Phyotnda kanstand Sonlar yani ozgarmas sonlaar yaratish uchun Ozgaruvchii katta
# harflar bilan yoziladi va bu ozgarivchiga tegilmaydi, ozgartirilmaydi\
    
    
radius=90
PI=3.14159 # Bu yerda PI qiymati ozgarmas son shuning uchun u kanstan son va katta harfda yoziladi
diametr=2*radius
print("Aylananing uzunligi:", PI*diametr)

ism="Narimon"
yosh=92 # agar bu yerdagi sonni ham ozgartirmoqchi bolsan unda::
yosh=str(yosh) # Endi bunda faylga qarasa son int emas str bolib qoladi
xabarnoma= ism+ ' ' +yosh+ ' ' +'yoshda' # bu codni bajarsa hato beradi sababi 
# matn bilan int birga + bilan boglab bolmaydi
print(xabarnoma) # Buni togrilasjh uchun sonni matnga otqazib olish kerak

# Sonni matnga otqazib olish uchun STR funksiyasidan foydalanamiz. Bunda yosh
#deb nomlangan funksiya  바꾸지가 않지만 숫자가 이제 문장으로 바꿔.
 
ism=" LIN"
yosh=27
xabarnoma=ism+'  '+str(yosh)+ '  '+ 'yoshda' # bu yerda yoshni str ozgartimasdan 
# faylda vaqtincha matnga ozgartirib olingani
print(xabarnoma) # endi faylga qararlsa yosh int da str ga otqazilmagan 
# keyinchalik ozgartirish imkoni bor

#t_yil=input("Tugilgan yilingizni kiriting?\n>>>") # Input funksiya har qanday
# sonni matnga aylantiriadi buni oldini olish uchun oldidan int funksiyasi ishlatildi
#yosh=str(2026-t_yil) # Bu yerda sonda mattni ayrib bolmaydi hato beradi dastur
#print("Siz", yosh, "yoshda enasiz!")


#t_yil=int(input("Tugilgan yilingizni kiriting?\n>>"))
#yosh=2026-t_yil
#print("Siz", yosh, "yoshda ekansiz!")

a= int("30")
e=float("81")
temp=str(30.4)