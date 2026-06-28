# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:23:50 2026

@author: ASUS
"""
import json #ozgaruvchilar stringda boladi
#import googlemaps
#rom apokey import APIKEY

##GoogleMaps
x=10
x_json=json.dumps(x)

y=5.5
y_json=json.dumps(y)


m=True
m_json=json.dumps(m) ##Bu jsonda matn phtonda yozilsa ham json bilan avval Java skriptga otadi keyin esa phytonga otadi


sonlar=(12,13,14,15,16) # Jsonda qiymat tortburchak korinishga otadi sabab javada tortburchak boladi
sonlar_json=json.dumps(sonlar)


#Loads() funksiyasi bilan javadan pydan otadi


bemor={
       "ism": 'Alijon VAliyev',
       'yosh':29,
       'oila':True,
       'farzandlar':('Nodir','Jamila'),
       'ellergiya':None,
       'dorilar':[
           {'nomi':'Analgin','miqdori':0.5},
           {'nomi':'Panadol', 'miqdori':1.2}
           ]
       }

##Jsonga otqazganda lugat matnga str ga ozgaradi lugat esa lugatligicha qoladi
#bemor_json=json.dumps(bemor)
#print(bemor_json)

bemor_json=json.dumps(bemor,indent=4) ## Bunda chiroyli qilib 4 qator kkatak tashlab chiqaradi
print(bemor_json)

with open('bemor.json','w') as f:
    json.dump(bemor,f)


with open('sonlar.json','w') as f:
    json.dump(sonlar,f)
    

bemor2=json.loads(bemor_json) # Bunda str dan dict ga otadi
 ##Bu format googlga malumot yuborganda va olganda kop ishlatiladi


## Json bilan ishlashda lugatlar bilan ishlash juda ham muhim













