# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)

# Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
# X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
# X este un int
#
# 1.
# Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# Daca conditia noastra este intalnita, programul v-a printa ceva, in caz contrat v-a printa altceva
#
# 2.
# Verifica si afiseaza daca x este numar natural sau nu
# x = int(input('x = '))
# if x > 0:
#     print('x este numar natural')
# else:
#     print('x nu este un numar natural')
# #
# # 3.
# # Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
#
# if x > 0:
#     print('x este nr pozitiv')
# elif x < 0:
#     print('x este numar negativ')
# else:
#     print('x este neutru')
# #
# # 4.
# # Verifica si afiseaza daca x este intre -2 si 13
#
# if x >= -2 and x <= 13:  # se scrie cu >, < daca este interval deschis
#     print('numarul este intre -2 si 13')
# else:
#     print('numarul nu este intre -2 si 13')  # nu stiu daca era necesar else
# #
# # 5.
# # Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# #
# y = int(input("y = "))
# if (x - y) < 5:
#     print('Diferenta dintre x si y este mai mica decat 5')
#
# # 6.
# # Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
#
# if not(x > 5 and x < 27):
#     print('x nu este intre 5 si 27')
# #
# # 7.
# # x si y (int)
# # Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
# #
# if x == y:
#     print('x este egal cu y')
# elif x > y:
#     print('x este mai mare decat y')
# else:
#     print('y este mai mare decat x')
# # 8.
# # X, y, z - laturile unui triunghi
# # Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
#
# z = int(input('z = '))
#
# if (x == y and x != z) or (x == z and x != y) or (y == z and x != z):
#     print('triunghiul este isoscel')
# elif x == y == z:
#     print('triunghiul este echilateral')
# else:
#     print('triunghiul este unul oarecare')
#
# 9.
# Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu

# lit = str.casefold(input('Scrieti o litera: '))
# if lit.isdigit() == True:
#     print('scrieti o litera')
# elif lit == 'a' or lit == 'e' or lit == 'i' or lit == 'o' or lit == 'u':
#     print('Litera este vocala')
# else:
#     print('Litera nu este vocala')
#
# 10.
# Transforma si printeaza notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
#
# n = int(input('Scrieti nota: '))
# if n > 10 or n < 1:
#     print('Scrieti o nota reala')
# elif n == 10:
#     n = 'A'            #  aici am suprascris n de fiecare data pentru ca zicea transformati.. probabil nu era nevoie
#     print('Nota este', n)
# elif  n == 9:
#     n = 'B'
#     print('Nota este', n)
# elif n == 8:
#     n = 'C'
#     print('Nota este', n)
# elif n == 7:
#     n = 'D'
#     print('Nota este', n)
# elif n >= 5 and n <= 6:
#     n = 'E'
#     print('Nota este', n)
# else:
#     n = 'F'
#     print('Nota este', n)
#

# c. Optionale (may need google)
#
# 11.
# Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = int(input('Scrieti un numar'))
# if x / 1000 > 1:                 # este fara len si mult mai simplu, sunt curios daca era si alta metoda fara len.
#     print('nr are minim 4 cifre')
# else:
#     print('numarul are mai putin de 4 cifre')

#
# 12.
# Verifica daca x are exact 6 cifre

# if x / 100000 > 1 and x / 100000 < 10:
#     print('Nr are exact 6 cifre')

#
# 13.
# Verifica daca x este numar par sau impar

# if x % 2 == 0:
#     print('x este nr par')
# else:
#     print('x este nr impar')
#
# 14.
# x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
#
# x = int(input('x= '))
# y = int(input('y= '))
# z = int(input('z= '))
# if x >= y and x >= z:
#     print(f'{x} este cel mai mare numar')
# elif y >= x and y >= z:
#     print(f'{y} este cel mai mare numar')
# else:
#     print(f'{z} este cel mai mare numar')
#

#
# 15.
# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
#
# x = int(input('unghiul x= '))
# y = int(input('unghiul y= '))
# z = int(input('unghiul z= '))
# if x + y + z == 180 and x > 0 and y > 0 and z > 0:
#     print('triunghiul este valid')
# else:
#     print('triunghiul nu este valid')

# 16.
# Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
#
# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
#
# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc
#
# vrs = int(input('Scrieti varsta:'))
# pasaport = True
# cu_mama = True
# cu_tata = True
# perm_mama = True
# perm_tata = False
#
# if vrs >= 18 and pasaport == True:
#     print('Ma pot imbarca')
# elif vrs < 18 and pasaport == True and cu_tata == True and cu_mama == True:
#     print('Ma pot imbarca')
# elif vrs < 18 and pasaport == True and cu_tata == True and perm_mama == True:
#     print('Ma pot imbarca')
# elif vrs < 18 and pasaport == True and cu_mama == True and perm_tata == True:
#     print('Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca')

# 17. Joc ghicit zarul
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# Luati un nr ghicit de la utilizator
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y
#
#
# import random
#
# dice_roll = random.randint(1,6)
# nr = int(input('Ghiciti numarul: '))
# if nr <= 6 and nr >= 1 and nr > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {nr} dar a fost {dice_roll}')
# elif nr <= 6 and nr >= 1 and nr < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {nr} dar a fost {dice_roll}')
# elif nr <= 6 and nr >= 1 and nr == dice_roll:
#     print(f'Felicitari! Ai ghicit. Ai ales {nr} si zarul a fost {dice_roll}')
# else:
#     print('Introduceti un numar intre 1 si 6')
#


