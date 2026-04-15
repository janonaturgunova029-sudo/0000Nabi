# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:50:18 2026

@author: ASUS
"""
mehmonlar=["Ali",'Doston','rustam',
           'Alisher']
#print(mehmonlar) #BUni qayta qayta yozib chiqishni orniga "FOR'
#tsiklidan foydalanamiz
#for mehmon in mehmonlar:  #bu yerda mehmon degan yangi ozgaruvchi yaratib uni ichiga
#mehmonlardagi ozgaruvchini yuklab chiqilayapti
  #print("Salom", mehmon)
  #print("yaxshi boring",mehmon)
  
  
#tana_azolar=['qol','oyoq','yelka','bilak']
#for t in tana_azolar:
#    print("odam azolariga kiradi:", t)
    
    
#yollar=['sariq yol', 'qiyshiq yol','tog\'riyol','qing\'ir yol']
#for yol in yollar:
   # print("odam hayotida shunday yullarga kirishi mumkin:", yol)
    #print('Tanlov odamga bogliq')
    
#mehmonlar=["Ali",'Doston','rustam',
#           'Alisher']
#for mehmon in mehmonlar:
    #print(f"Hurmatli {mehmon} sizni 20 kuni boladigan bazmga taklif qilamiz!")
    #print("hurmat bilan G\'niyevlar oilasi")
    
    
#sonlar=list(range(0,11)) 
#for son in sonlar:
    #print(f"{son} ning kvadrati {son**2} ga teng")

#raqamlar=list(range(0,9))
#for son in raqamlar:
#    print(f"{son} ning kubi {son**3} ga teng")


#sonlar=list(range(11))
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
    
#print(sonlar)
#print(sonlar_kvadrati)

dostlar=[]
print("5 ta eng yaqin dostingiz kim?")
for n in range(5):
    
    dostlar.append(input(f"{n+1}-dostingizni ismini kiriting:"))
    print(dostlar)
                         