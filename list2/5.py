# Szymon Fica 337307
# list 2, task 5

def kompresja(tekst):
    ans = []
    i = 0
    while i < len(tekst):
        j = i
        while j+1 < len(tekst) and tekst[i] == tekst[j+1]:
            j += 1
        #print(str(j) + " " + tekst[i])
        ans.append((j-i+1, tekst[i]))
        i = j
        i += 1
    return ans

def dekompresja(tekst_skompresowany):
    ans = ""
    for i in tekst_skompresowany:
        for j in range(0, i[0]):
            ans += i[1]
    return ans

a = kompresja("aaabbcde")
print(a)
b = dekompresja(a)
print(b)

print("dekompresja(kompresja(\"aaabbcde\")) == \"aaabbcde\": " + str(dekompresja(kompresja("aaabbcde")) == "aaabbcde"))

# link do tekstu: https://wolnelektury.pl/katalog/lektura/pan-tadeusz.html

tadeusz = "Litwo! Ojczyzno moja! ty jesteś jak zdrowie:\
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

#a = kompresja(tadeusz)
#print(a)
#b = dekompresja(a)
#print(b)

print("dekompresja(kompresja(tadeusz)) == tadeusz: " + str(dekompresja(kompresja(tadeusz)) == tadeusz))