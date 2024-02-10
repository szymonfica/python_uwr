# Szymon Fica 337307
# list 5 task 2

class Formula:

    def oblicz(self, zmienne):
        pass

    def __str__(self):
        return "Formula"

    def __add__(self, F):
        return Or(self, F)
    
    def __mul__(self, F):
        return And(self, F)
    
    def tautologia(self):
        zmienne = list(set(self.lista_zmiennych()))
        for i in range(2**len(zmienne)):
            values = {}
            for j in range(len(zmienne)):
                values[zmienne[j]] = bool(i & (1 << j))
            if not self.oblicz(values):
                return False
        return True

    def lista_zmiennych(self):
        return []

class And(Formula):
    def __init__(self, L, R):
        if not isinstance(L, Formula) or not isinstance(R, Formula):
            raise ValueError("Argumenty And() nie sa Formula")
        self.L = L
        self.R = R

    def oblicz(self, zmienne):
        return self.L.oblicz(zmienne) and self.R.oblicz(zmienne)
    
    def __str__(self):
        return "(" + self.L.__str__() + " and " + self.R.__str__() + ")"

    def lista_zmiennych(self):
        return self.L.lista_zmiennych() + self.R.lista_zmiennych()
    

class Or(Formula):
    def __init__(self, L, R):
        if not isinstance(L, Formula) or not isinstance(R, Formula):
            raise ValueError("Argumenty Or() nie sa Formula")
        self.L = L
        self.R = R 

    def oblicz(self, zmienne):
        return self.L.oblicz(zmienne) or self.R.oblicz(zmienne)
    
    def __str__(self):
        return "(" + self.L.__str__() + " or " + self.R.__str__() + ")"

    def lista_zmiennych(self):
        return self.L.lista_zmiennych() + self.R.lista_zmiennych()
    
   

class Zmienna(Formula):
    def __init__(self, nazwa):
        if not isinstance(nazwa, str):
            raise ValueError("Bledna nazwa zmiennej")
        self.nazwa = nazwa

    def oblicz(self, zmienne):
        if self.nazwa not in zmienne:
            raise ValueError("Bledna nazwa zmiennej")
        return zmienne[self.nazwa]
    
    def __str__(self):
        return self.nazwa
    
    def lista_zmiennych(self):
        return [self.nazwa] 
    

class Stala(Formula):
    def __init__(self, wartosc):
        if wartosc != True and wartosc != False:
            raise ValueError("Wartosc stalej musi byc True/False")
        self.wartosc = wartosc

    def oblicz(self, zmienne):
        return self.wartosc
    
    def __str__(self):
        return str(self.wartosc)

    
class Not(Formula):
    def __init__(self, F):
        if not isinstance(F, Formula):
            raise ValueError("Argumentem Not() musi byc Formula")
        self.F = F

    def oblicz(self, zmienne):
        return not self.F.oblicz(zmienne)
    
    def __str__(self):
        return "(not " + self.F.__str__() + ")"

    def lista_zmiennych(self):
        return self.F.lista_zmiennych()
    

print(And(Zmienna('B'), Not(Zmienna('B'))).tautologia())
print(Or(Zmienna('C'), Not(Zmienna('C'))).tautologia())
print(And(Zmienna('A'), Or(Zmienna('C'), Stala(True))).tautologia())
print(And(Or(Stala(True), Zmienna('A')), Or(Zmienna('C'), Stala(True))).tautologia())

print(Zmienna("x") + Zmienna("y"))
print(Zmienna("x") * Zmienna("y"))