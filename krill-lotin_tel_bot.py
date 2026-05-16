# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:00:07 2026

@author
"""
## ISASCII( ) USULI BILAN MATNNI QAYSI KLAVIATURA BILAN YOZAYOTGANIMIZNI BILIB OLSAK BOLADI
from transliterate import to_cyrillic, to_latin
#print(to_cyrillic('dastur'))
matn=input('Matn kiriting:')

if matn.isascii():
   print(to_cyrillic(matn))
else:
    print(to_latin(matn))


































