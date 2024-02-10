# Szymon Fica 337307
# list 3 task 5

def max_sublist_sum(lista):
    if len(lista) == 0:
        return (0, 0)
    p, q, ms, cs, cp, cq = 0, 0, 0, 0, 0, 0
    for i in range(0, len(lista)):
        if lista[i] < cs + lista[i]:
            cs += lista[i]
            cq = i
        else: 
            cs = lista[i]
            cp, cq = i, i
        if cs > ms:
            ms = cs
            p, q = cp, cq
    return (p, q)


lista = [12, -13, 1, 2, 3, -4, 5, 6, -7, 1]

print("max_sublist_sum(" + str(lista) + ") = " + str(max_sublist_sum(lista)))
