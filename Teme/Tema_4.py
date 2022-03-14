# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Iteratiile sunt greute, deoarece necesita putina gandire algoritmica
# Va rog sa imi scrieti pe slack unde intampinati dificultati si va ajut
# Daca stati blocati > 30 min, cereti indiciu
#
# b. Dificultate medie (Faceti cat puteti din ele)
#
# 1.
# Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while
#
# for i in range(len(masini)):
#     print(f'{masini[i]} este masina mea preferata')   # am folosit for
#
# for masina in masini:
#     print(f'{masina} este masina mea preferata')      # am folosit for each

# i=0
# while i <= len(masini)-1:
#     print(f'{masini[i]} este masina mea favorita')    # am folosit while
#     i = i + 1


# 2.
# Aceeasi lista
# Folositi un for else
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else
#    Printati lista

# for i in range(len(masini)):
#     masini[i] = masini[i].upper()
#     masini[0] = masini[0].casefold()
#     masini[len(masini) - 1] = masini[len(masini) - 1].casefold()
# else:
#     print(masini)

# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

# for i in range(len(masini)):
#     if masini[i] == 'Mercedes':
#         print('Am gasit masina dorita de dvs, un Mercedes')
#         break
#     else:
#         print(f'Am gasit masina {masini[i]}, mai cautam')
#
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
# Iterati prin lista
#
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
#
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa masina {masini[i]}')

# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’
# Printati Modele vechi: x
# Modele noi: x
#

# masini_vechi = []
#
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# else:
#         print(masini)
#         print(masini_vechi)

# 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x

# for masina, pret in pret_masini.items():
#     if pret <= 15000:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina}')
# 7.
# Avand
#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
# counter = 0
# for i in range(len(numere)):
#     if numere[i] == 3:
#         counter = counter + 1
#print(f'numarul 3 apare de {counter} ori')
#
# 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
#
# s = 0
# for i in range(len(numere)):
#     s = s + numere[i]
# print(f'suma numerelor este {s}')
#

#
# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
#
# nr = 0
# for i in range(len(numere)):
#     if numere[i] > nr:
#         nr = numere[i]
#print(f'Cel mai mare numar este {nr}')
#
# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
#
# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere[i] = -abs(numere[i])
#print(numere)
#
#
#
# c. Optionale (may need google)
#
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final
#
# for i in range(len(alte_numere)):
#     if alte_numere[i] % 2 == 0:
#         numere_pare.append(alte_numere[i])
#     elif alte_numere[i] % 2 != 0:
#         numere_impare.append(alte_numere[i])
#     if alte_numere[i] > 0:
#         numere_pozitive.append(alte_numere[i])
#     else:
#         numere_negative.append(alte_numere[i])
# print(f'Numerele pare sunt: {numere_pare}')
# print(f'Numerele impare sunt: {numere_impare}')
# print(f'Numerele pozitive sunt: {numere_pozitive}')
# print(f'Numerele negative sunt: {numere_negative}')

# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)

# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
#
import random

# numar_secret = random.randint(1, 30)
# numar_ghicit = None
# while numar_ghicit == None:
#     numar= int(input('Alege un numar:'))
#     if numar < 1 or numar > 30:
#         print('Alege un nr intre 1 si 30')
#     elif numar > numar_secret:
#         print('Numarul introdus este mai mare')
#     elif numar < numar_secret:
#         print('Numarul introdus este mai mic')
#     else:
#         print('Felicitari! Ai gasit numarul')
#         numar_ghicit = numar_secret
# #
# 14.
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

# nr = int(input('Scrieti un numar:'))
# for i in range(1,nr+1):
#     print(i, end='')
#     print('')
#
# numar = int(input("Scrie un nr: "))
#
# for i in range(1,numar+1):
#     for j in range(i):
#         print(i , end="")
#     print("\n ")

# 15.
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)
#
# for i in range(len(tastatura_telefon)):
#    for j in range(len(tastatura_telefon[i])):
#        print(f'Cifra curenta este {tastatura_telefon[i][j]}')