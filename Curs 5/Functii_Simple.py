# FUNCTIA SIMPLA
# o zona de cod cu logica proprie, care poate fi folosita/refolosita (apelata) de oricate ori avem nevoie
# write once, use n times

def say_hi ():
    print('Hi')

say_hi()
say_hi()

x = say_hi()
print(x)    # nu poate printa ceva ce nu returneaza nimic

# FUNCTIA CU PARAMETRU
# face ceva si poate sa aiba date de intrare diferite ca sa folosesti functia pt ce date vrei tu
# param se despart de virgula

def print_hi(nume, prenume):
    prenume = prenume.upper()
    print(f'Hi {nume} {prenume}!')

print_hi('Denis', 'Morariu')

# FUNCTIA CU RETURN

# functia ne da si un raspuns(output)
# putem salva respunsul in variabile
# se poate returna orice tip de date
# Return e ultimul lucru din functie
# avem un singur return in general, EXCEPTIE cand avem if, else
# lovechild between break + pop

# input 5 numere
# output ne dorim un set

def make_set(n1, n2, n3):
    r = set()
    r.add(n1)
    r.add(n2)
    r.add(n3)
    return r


set_2 = make_set(1, 2, 2)
set_1 = make_set(1, 2, 3)
print(set_1.intersection(set_2))

# cand apelex functia eu deja trebuie sa vizualizez rezultatul

print(make_set(1,2,3).intersection(make_set(2,3,4)))

def pi_value():
    return 3.14

x = pi_value() + 4
print(x)

# import suma din helpers
from folder1.helpers import * # importez orice functie din folder si e varianta ideala


# import tot din helpers

from folder1 import helpers

suma(3,4)
print(suma(3,4))

