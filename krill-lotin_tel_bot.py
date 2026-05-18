# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:00:07 2026

@author
""" #qushchalar qanot qoqib osmonda erkin uchmoqda
## ISASCII( ) USULI BILAN MATNNI QAYSI KLAVIATURA BILAN YOZAYOTGANIMIZNI BILIB OLSAK BOLADI
from transliterate import to_cyrillic, to_latin
import telebot

TOKEN='8717679004:AAHhez6CrcRV7gDYEGF9n1xIwqXAaFVWD38'
bot=telebot.TeleBot(TOKEN,parse_mode=None)
#TOKEN=8717679004:AAHhez6CrcRV7gDYEGF9n1xIwqXAaFVWD38
#print(to_cyrillic('dastur'))
#matn=input('Matn kiriting:')
@bot.message_handler(commands=['start']) # Bu yerda message hendler shunday turdagi habar ucun pastidagi funksiya masul bolishini anglatadi
def send_welcome(message):
    bot.reply_to(message, "Howdy, How are you doing?")
bot.polling()

#if matn.isascii():
#   print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))


































