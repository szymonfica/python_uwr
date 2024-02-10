# Szymon Fica
# list 1 task 1

import decimal as d

def vat_faktura(lista):
    ans = 0
    for i in lista:
        ans += i
    ans = 1.23 * ans
    return ans

def vat_paragon(lista):
    ans = 0
    for i in lista:
        ans += 1.23 * i
    return ans

def vat_faktura_dec(lista):
    ans = 0
    for i in lista:
        ans += i
    ans = d.Decimal("1.23") * ans
    return ans

def vat_paragon_dec(lista):
    ans = 0
    for i in lista:
        ans += d.Decimal("1.23") * i
    return ans

zakupy = [1.0, 2.0, 3.0, 0.00000813]
zakupy_dec = [d.Decimal(1.0), d.Decimal(2.0), d.Decimal(3.0), d.Decimal(0.00000813)]

print("Obliczenia na typie float: ")
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))

print(vat_faktura(zakupy) == vat_paragon(zakupy))

print()
print("Obliczenia na typie Decimal: ")
print(vat_faktura_dec(zakupy_dec))
print(vat_paragon_dec(zakupy_dec))

print(vat_faktura_dec(zakupy_dec) == vat_paragon_dec(zakupy_dec))


