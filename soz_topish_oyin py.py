# SOZ TOP OYINI KOD
import random
from uzwords import words

def get_word():
    word=random.choice(words)
    while "-" in word or ' ' in word: # Agar lugatd shunday belgilar bolsa"
    # unda shuni pastdagidek yana qaytadan chaqirib olayapti
        word=random.choice(words)
    return word.upper()


def display(user_letters,word): # Bu funksiyasini vazifasi foydalanuvchi topgan harflarini qaytarib chiqarib beradi
    display_letter=' '
    for letter in word:
        if letter in user_letters.upper():
            display_letter+=letter
        else:
            display_letter+="-"
    return display_letter

def play():
    word=get_word()
    word_letters=set(word)  # setdan foydalanishga sabab qaytarilgan sozlar bomasdan chiqarib beradi
    user_letters=''                        ## Soz ichidagi harflarni ikkita bir xil qatnashgan bolsa birini ochirib faqat bittasini chiqarib berDI
    print(f'Men {len(word)} xonali son oyladim. Topa olasizmi?')
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f'Shu vaqtgacha kiritgan harflaringiz: {user_letters}')
















