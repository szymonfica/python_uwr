# Szymon Fica 337307
# list 2 task 4

import random

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    words = tekst.split()
    zdanie = []
    for s in words:
        if(len(s) <= dl_slowa):
            zdanie.append(s)
    while len(zdanie) > liczba_slow:
        del zdanie[random.randint(0, len(zdanie)-1)]
    ans = ""
    for s in zdanie:
        ans += (s + " ")
    return ans

tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."

print(uprosc_zdanie(tekst, 10, 15))

# link do tekstu: https://wolnelektury.pl/katalog/lektura/pan-tadeusz.html

tekst = "Litwo! Ojczyzno moja! ty jesteś jak zdrowie:\
Ile cię trzeba cenić, ten tylko się dowie, \
Kto cię stracił. Dziś piękność twą w całej ozdobie\
Widzę i opisuję, bo tęsknię po tobie. \
Panno święta, co Jasnej bronisz Częstochowy\
I w Ostrej świecisz Bramie! Ty, co gród zamkowy\
Nowogródzki ochraniasz z jego wiernym ludem!\
Jak mnie dziecko do zdrowia powróciłaś cudem\
(Gdy od płaczącej matki, pod Twoją opiekę\
Ofiarowany, martwą podniosłem powiekę;\
I zaraz mogłem pieszo, do Twych świątyń progu\
Iść za wrócone życie podziękować Bogu),\
Tak nas powrócisz cudem na Ojczyzny łono. \
Tymczasem przenoś moją duszę utęsknioną\
Do tych pagórków leśnych, do tych łąk zielonych,\
Szeroko nad błękitnym Niemnem rozciągnionych;\
Do tych pól malowanych zbożem rozmaitem,\
Wyzłacanych pszenicą, posrebrzanych żytem;\
Gdzie bursztynowy świerzop, gryka jak śnieg biała,\
Gdzie panieńskim rumieńcem dzięcielina pała,\
A wszystko przepasane jakby wstęgą, miedzą\
Zieloną, na niej z rzadka ciche grusze siedzą."

print(uprosc_zdanie(tekst, 10, 15))