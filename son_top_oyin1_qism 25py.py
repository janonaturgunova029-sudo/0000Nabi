# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:55:09 2026

@author: ASUS
"""

import random

def son_top(x=10):
    tasodifiy_son=random.randint(1,x) #RANDINT() BERILGAN ORALIQDAGI BITTA BUTUN SONNI QAYTARADI
    print(f"Men 1 dan {x} gacha son oyladim. Topa olasizmi?")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin=int(input('>>>'))
        if taxmin<tasodifiy_son:
            print('Xato, men o\'ylaga son bundan kattaroq, Yana harakat qiling:')
        elif taxmin>tasodifiy_son:
            print('Xato, men oylagan son bundan kichikroq, yana harakat qiling:')
        else:
            break  
    print(f'Tabriklaymiz, {taxminlar} taxmin bilan topdingiz')
    return taxminlar 



def son_top_pc(x=10):
    input(f'1 dan {x} gacha son oylang va istalgan tugmani bosing, '\
        f'Men topaman:')
    quyi=1
    yuqori=x 
    taxminlar=0
    while True:
         taxminlar+=1
         if quyi!=yuqori: 
             taxmin=random.randint(quyi,yuqori)
         else:
             taxmin=quyi
         javob=input(f'Siz {taxmin} sonni oyladingiz: togri(t),'\
                        f'men oylagan son bundan kattaroq(+),yoki kichikroq(-):'.lower())     
         if javob=="-":
            yuqori=taxmin-1
         elif javob=="+":
            quyi=taxmin+1
         else:
            break
    print(f'Men {taxminlar} taxmin bilan topdim')
    return taxminlar














