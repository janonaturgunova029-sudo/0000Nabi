# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:01:19 2026

@author: ASUS
"""
import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon','valiyev')
        self.assertEqual(name,'Alijon Valiyev')
        
    def test_otasining_ismi(self):
        name=get_full_name('alijon','valiyev','olimovich')
        self.assertEqual(name,'Alijon Valiyev Olimovich')
        
unittest.main()






