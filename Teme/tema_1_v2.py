# 1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
#
# b. Usor spre Mediu (obligatoriu)
# 1.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
#
# o variabila este un spatiu din memorie care tine date

# 2.
# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
# masina = 'Audi' # string
# an_fabricatie = 2013 # int
# greutate_tone = 1.9 # float
# masina_noua = False # boolean
#
# print(f'{masina} din anul {an_fabricatie} cu greutatea de: {greutate_tone} tone')
# print('masina este noua?', masina_noua)
#
# # 3.
# # Utilizat functia type pentru a verifica ca ele au tipul de date asteptat
#
# print(type(masina)) # trebuie sa fie string
# print(type(an_fabricatie)) # trebuie sa fie int
# print(type(greutate_tone)) # trebuie sa fie float
# print(type(masina_noua)) # trebuie sa fie bool
# #
# # 4.
# # Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# # Verificati tipul acesteia
#
# greutate_noua = round(greutate_tone)
# greutate_tone = greutate_noua
# print('greutatea rotunjita este: ',greutate_tone)
# if type(greutate_tone) == int:
#     print('variabila este de tipul: int')
# #
# # 5.
# # folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# # (rezolvati nepotrivirile de tip prin ce modalitate doriti)
#
# print(f'{masina} din anul {an_fabricatie} cu greutatea de: {greutate_tone} tone')
# print('masina este noua?', masina_noua)
#
# if masina_noua == True:
#     print('masina este noua')
# else:
#     print('masina nu este noua') # aici doar incercam
#
# # 6.
# # citeste de la tastatura numele
# nume = input('Introduceti numele: ')
#
# # citeste de la tastatura prenumele
#
# prenume = input('Introduceti prenumele: ')
#
# # afiseaza 'Numele complet are x caractere'
# print('Numele complet are', len(nume) + len(prenume), 'caractere'

#
# 7.
# citeste de la tastatura lungime

# lungime = int(input('lungimea triunghiului este: '))

# citeste de la tastatura latimea

# latime = int(input('latimea triunghiului este: '))
#
# # afiseaza 'Aria dreptunghiului este x'
# aria = lungime * latime
# print(f'aria dreptunghiului este: ', aria)

# 8.
# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'

propozitie = 'Coral is either the stupidest animal or the smartest rock'

# cititi de la tastatura un int x

#x = int(input('cate caractere stergem?' ))

# afiseaza stringul fara ultimele x caractere
# y= len(propozitie)

# print(propozitie[:y-x])

# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
#
# 9.
# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5
# propozitite_noua = propozitie[:4] + propozitie[y-5:]
# print(propozitite_noua)
# print(propozitie[:4], propozitie[y-5:])

# 10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'

# print(propozitie.count('the'))
#
# 11.
# acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul
# propozitie=propozitie.replace(' the', ' THE')
# print(propozitie)
#
# 12.
# acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# i = propozitie.index('rock')
# print(i)

# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
# print(propozitie[:i])
# #
# # 13.
# # citeste de la tastatura un string
#
# cuvant = str.casefold(input('Scrie: '))  # am folosit casefold ca sa transforme orice scrie in litere mici
#
# # verifica daca primul si ultimul caracter sunt la fel
# # se va folosi un assert
# l = len(cuvant)
# assert cuvant[:1] == cuvant[l-1:l]
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

# 14.
# avand stringul '0123456789'
# afisati doar numerele pare
# my_string = '0123456789'
# print(my_string[:4])
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
# x = '0123456789'
# print(x[2::2])
# print(x[1::2])
#
# 15.  # nu am stiut
# acelasi string de la 12
# folositi un assert ca sa verificati daca acest string contine doar numere
# hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare

# assert propozitie.isdigit() == True

# c. Optionale (may need google)
# 16.
# citeste de la tastatura un string de dimensiune impara
# # afiseaza caracterul din mijloc
# cuvant = str(input('cuvand de dimensiune impara'))
# x = len(cuvant)
# print(x)
# y= int((x-1)/2)
# print(cuvant[y])

# 17.
# Folosind assert, verificati daca un string este palindrom
# cuvant = 'ana'
# assert cuvant == cuvant[::-1]

# 18. # nu am stiut
# folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare
#
input('Scrieti:')
x = input[]
print(x)

# 19.
# citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)

# cuvinte = input('Scrie 2 cuvinte')
# first_char = cuvinte[0]
# last_char = cuvinte[len(cuvinte)-1]
# x=int(len(cuvinte))-1
# new_cuvinte = cuvinte[1:x]
# first_char_new=first_char.upper()
# new_cuvinte_2=new_cuvinte.replace(first_char,first_char_new)
# print(new_cuvinte_2)
# cuvinte_finale=first_char + new_cuvinte_2 + last_char
# print(cuvinte_finale)

# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla
#
# 20.
# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

# username = input('introdu user: ')
# password = input('introdu parola: ')
# hidden_password = '*' * len(password)
# print(f'parole pentru userul {username} este {hidden_password} si are {len(password)} caractere.')