# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:50:36 2026

@author: ASUS dars phaytn 존라 하고 싶지 않지만 나의 미래 네가 속상하고 후외하지 않으려면from
"""
#file=open('pi.txt')
#PI=file.read()
#print(PI)
#file.close()


with open('pi.txt') as file:
    pi=file.read()
    
print(pi)    

pi=pi.rstrip() ##qator oxiridagi boshliqni olib tashladik
pi=pi.replace('\n','') ##Qatorlarni olib tashlaydu
#pi = float(pi) #Bu esa pi raqamlarni songa otqazadi

print(pi)











