# Szymon Fica 337307
# list 2 task 1

def f(wynik_wyborow, miejsca):
    tab = []
    sum = 0
    for i in wynik_wyborow:
        sum += i[1]
    for i in wynik_wyborow:
        if i[1]*100 >= 5*sum:
            for j in range(1, miejsca+1):
                tab.append((i[1]/j, i[0]))
    tab.sort(reverse=True)
    while len(tab) > miejsca:
        tab.pop()
    return tab
  

votes = [("A", 720), ("B", 300), ("C", 480)]

a = f(votes, 8)
print(a)