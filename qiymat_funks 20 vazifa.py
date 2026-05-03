# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:14:20 2026

@author: ASUS
"""
    #1
#def malumot_sora(ismi,familiyasi,t_yili,t_joyi,e_manzili=' ', tel_raqami=None):
#      """Mijozlar haqida malumot olib lugat korinishida qaytaruvchi dastur"""
#      mijoz={'ismi':ismi,
#             'familiyasi':familiyasi,
#             't_yili':t_yili,
#             'yoshi':2026-t_yili,
#             't_joyi':t_joyi,
#             'e_manzili':e_manzili,
#             'tel_raqami':tel_raqami}
#      return mijoz

#print('Foydalanuvchining malumotlari:')
#mijozlar=[ ]
#while True:
#    ismi=input('Ismi;')
#    familiyasi=input('Familiyasi:')
#    t_yili=int(input('t_yili:'))
#    t_joyi=input('t_joyi:')
#    e_manzili=input('E_manzil:')
#    tel_raqami=input('Traqam:')
#    mijozlar.append(malumot_sora(ismi,familiyasi,t_yili,t_joyi,e_manzili))
#    javob=input('Davom ettirasizmi? (ha\yoq)')
#    if javob=='yoq':
#        break
#print('Mijozlar:')
#for mijoz in mijozlar:
#    print(f'{mijoz['ismi'].title()} {mijoz['familiyasi'].title()}\n'
#           f'{mijoz['yoshi']} yoshda, E-manzili {mijoz['e_manzili']}' 
#           f'{mijoz['t_joyi'].title()}da tugilgan'
#          f'Telefoni:{mijoz['tel_raqami']}')
   

# 3 savol
#def kattasi(x,y,z):
#    max=x
#    if y>=max:
#        max=y
#    if z>=max:
#        max=z
#    return max
        
#print(kattasi(10,1,-12))
         
 

# 5 savol       
#def tub_son_top(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         tub=True
#         if (n==1):
#            tub=False
#         elif(n==2):
#           tub==True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub=False
#         if tub:
 #            tub_sonlar.append(n)
#             
#     return tub_sonlar

#tub_son_top(1,10)        
         
#     return sonlar

#print(oraliq(1,10))
def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

tub_sonlar_top(1,20)































