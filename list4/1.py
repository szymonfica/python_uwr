# Szymon Fica 337307
# list 4 task 1

from math import floor, sqrt
import timeit

def pierwsze_imperatywna(n):
    ans = []
    for i in range(2, n+1):
        w = True
        for j in ans:
            if i%j == 0:
                w = False
        if w:
            ans.append(i)
    return ans

def pierwsze_skladana(n):
    return [x for x in range(2, n+1) if [ y for y in range(2, floor(sqrt(x)) + 1) if x % y == 0] == [] ]

def pierwsze_funkcyjna(n):
    return list( filter(lambda x : [ y for y in range(2, floor(sqrt(x)) + 1) if x % y == 0] == [] , range(2, n+1) ))

def pierwsze():
    print("n     imperatywna     skladana    funkcyjna     ", end = "\n")
    for i in range(1000, 10000, 1000):
        t1 = timeit.timeit(lambda : pierwsze_imperatywna(i), number = 10)
        t2 = timeit.timeit(lambda : pierwsze_skladana(i), number = 10)
        t3 = timeit.timeit(lambda : pierwsze_funkcyjna(i), number = 10)
        print("%1d: %11.7f %12.7f %12.7f"% (i, t1, t2, t3), end = "\n")


print(pierwsze_imperatywna(29))
print(pierwsze_skladana(29))
print(pierwsze_funkcyjna(29))
pierwsze()



