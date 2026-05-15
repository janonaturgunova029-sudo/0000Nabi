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

def play(): ##words lugatini ichidan tasodifiy sozni olish funksiyasi
    word=get_word() # Get word degan funsiyani ichiga random choice qilib yuklagan sozni bu yerda word degan ozgarucgia yuklayapti
    word_letters=set(word)  # setdan foydalanishga sabab qaytarilgan sozlar bomasdan chiqarib beradi
    user_letters='' 
##Bu yerda foydalanuvchi kiritgan sozlarni us-lettni ichiga yuklab boriladi                       ## Soz ichidagi harflarni ikkita bir xil qatnashgan bolsa birini ochirib faqat bittasini chiqarib berDI
    print(f'Men {len(word)} xonali soz oyladim. Topa olasizmi?')
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
           print(f'Shu vaqtgacha kiritgan harflaringiz: {user_letters}')

        letter=input("Xarf kiriting:").upper()
        if letter in user_letters:
            print('Bu harfni avval kiritgansiz. Boshqa harf kiriting!')
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarf togri.")
        else:
        print('Bunday harf yoq.')
        user_letters+=letter
    print(f'Tabriklayman! {word} sozini {len(user_letters)} ta urinishda topdingiz!')














