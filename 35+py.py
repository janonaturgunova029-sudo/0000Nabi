# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:10:42 2026

@author: ASUS
"""

# Hatolar bilan ishlash try-exept 35 dars


#yosh=input("Yoshingizni kiriting: ")
#try:
#   yosh=int(yosh)
#   print(f"Siz {2026-yosh} yilda tugilgansiz")
#except ValueError:
#    print("Butun son kiriting iltimos!")
    
    #Zero divitsion error
#x,y=5,10
#try: 
#    y/(x-5)    
#except ZeroDivisionError:
#    print("0 ga bolib bolmaydi")

#mevalar=['olma','anor','orik','shaftoli']
#try:
#   print(mevalar[3].title())
#except IndexError:
#    print(f"Royxatda {len(mevalar)} ta meva bor xolos")     



#user={"username":"memo",
#      "status":'admin',
#      'email':'smhhd22@Gma',
#      'phone':'010652321'}


#key='tel'

#try:
#    print(f"Foydalanuvchi: {user[key]}")
#except KeyError:
#    print('Bunday kalit mavjud emas')
    
#print(user['username'])


#filename="data.txt"
#try:
#    with open(filename) as f:
#        text=f.read()
#except FileNotFoundError:
#    print(f"{filename} mavjud emas")



#import json
#files=['talaba1.json','talaba2.json','talaba3.json']
#for filename in files:
#    try:
#        with open(filename) as f:
#            talaba=json.load(f)
#    except FileNotFoundError:
#        pass
#    else:
#        print(talaba['ism'])


#n=input('Butun son kiriting: ')
#try:
#    n=int(n)
#    x=8/n
#except ValueError:
#    print('Butun son kiritmadingiz')
#except ZeroDivisionError:
#    print("0 ga bolish vashshe mumkinmas, qolingni sindiraman bolmoqchi bolsang!!!!")
#else:
#    print(f"x={x}")

while True:
    yosh=input('Yoshingizni kiriting; ')
    if yosh.isdigit(): # bu metod  matnni raqamladan ibotatmi yoqmi tekshiradi
        yosh=int(yosh)
        break
print(f"Siz {2026-yosh} da tugilib qolgansiz ekan!! ")
        


















