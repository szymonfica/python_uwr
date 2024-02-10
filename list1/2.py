# Szymon Fica
# list 1 task 2

import math

def is_palindrom(text):
    text = (''.join(letter for letter in text if letter.isalnum())).lower()
    for i in range(math.floor(len(text)/2)):
        if text[i] != text[len(text)-i-1]:
            return False
    return True


print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))

string = "Ab,ca"
print(is_palindrom(string))