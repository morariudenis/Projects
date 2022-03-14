name = 'Andy'
nume_as_list = ['A', 'n', 'd', 'y']
# cum accesam un element
print(nume_as_list[0])
# len
print(len(nume_as_list))
# merge slicing? da
print(nume_as_list[0:2])
# cum scoatem un caracter?
nume_as_list.remove('n') # in fct de valoare
print(nume_as_list)
# ce face .pop
#Remove and return item in fct de index(default este ultimul)
# litera = nume_as_list.pop()
# print(litera)

print(nume_as_list.pop())
print(nume_as_list)
# cum suprascriem?
nume_as_list[0] = 'a'
# cum adaugam la index?
nume_as_list.insert(0, 'A')
print(nume_as_list)
# cum adaugam la final?
nume_as_list.append('s')
print(nume_as_list)
# cum facem replace? TEMA dupa ce invatam parcurgerea repetitiva a unei liste

# putem pune o lista in alta lista>? (lista 2d)
lista_in_lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# cum afisez 7
randul_3 = lista_in_lista[2]
print(randul_3[0])
#sau
print(lista_in_lista[2][0])

# sa luam la nimereala
lista2 = ['tel1', 'tel2', 'tel3']
import random

random_no = random.randint(0,len(lista2)-1)
# dau click
print(lista2[random_no])

lista3 = ['a', 'n', 'a'] # putem pune valori duplicat
print(lista3)
