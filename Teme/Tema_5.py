# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Pentru toate exercitiile
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
#
# b. Dificultate: usor spre mediu
#
# 1. Functie care sa calculeze si sa returneze suma a 2 numere

# def suma(a,b):
#     return a+b
#
# print(suma(4,5))
#
# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

# def numar(a):
#     if a % 2 == 0:
#         return 'TRUE'
#     else:
#         return 'FALSE'
#
# print(numar(11)) # primesc FALSE
#
# print(numar(12)) # primesc TRUE

#
# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

# numele = input('Scrieti numele: ')
# def nume(nume_input):
#     counter = 0
#     for i in range(len(nume_input)):     # STIU CA NU ASA TREBUIA, DAR AM VRUT SA MA COMPLIC
#         if nume_input[i] == ' ':
#             continue
#         else:
#             counter = counter +1
#     return counter
#
# print(nume(numele))


# def nume1(nume, prenume, nume_mij):
#     return len(nume) + len(prenume) + len(nume_mij)   #  L-AM FACUT SI ASA :)
#
# print(nume1('Morariu', 'Denis', 'Laurentiu'))

# 4. Functie care returneaza aria dreptunghiului

# def arie_dreptunghi(l, h):
#     return l*h
#
# print(arie_dreptunghi(5,5))

# 5. Functie care returneaza aria cercului
# import math
# PI = math.pi
# def arie_cerc(r):
#     return PI * r**2            # puteam sa si declar PI = 3.14 variabila globala, dar e mai distractiv asa
#                                 # tot uit cum se reduce la 2 decimale si daca il tot folosesc poate tin minte
# print("{:0.2f}".format(arie_cerc(3)))

#
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
# def carcacter(x, string_input):
#     for i in range(len(string_input)):
#         if string_input[i] == x:
#             return True
#     else:
#         return False
#
# print(carcacter('n', 'denis'))

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
#
# def character_counter(my_string):
#     count_lower = 0
#     count_upper = 0
#     for i in range(len(my_string)):
#         if(my_string[i] >= 'a' and my_string[i] <= 'z'):
#             count_lower = count_lower + 1
#         elif(my_string[i] >= 'A' and my_string[i] <= 'Z'):
#             count_upper = count_upper + 1
#     print(f'Nr de caractere lower case este: {count_lower}')
#     print(f'Nr de caractere upper case exte: {count_upper}')
#
# character_counter('AlaBalaPortocala')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#
# list1 = [3, 4, -2, -4, -5, 3, -1, 6]
# list2 = []
# def list_pos(lista1, lista2):
#     for i in range(len(lista1)):
#         if  lista1[i] > 0:
#             lista2.append(lista1[i])
#     return lista2
#     print(f'Lista cu numere pozitive este: {lista2}')
#
# print(list_pos(list1, list2))

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
#

# def numere(a, b):
#     if a > b:
#         print(f'Primul numar {a} este mai mare decat al doilea nr {b}')
#     elif b > a:
#         print(f'Al doilea nr {b} este mai mare decat primul nr {a}')
#     else:
#         print('Numerele sunt egale')
#
# numere(5,5)
# numere(4,5)
# numere(4,3)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
#
# setul = {1, 4, 5, 35, 234, 13, 2 }
# def numere(a, my_set):
#     before = len(my_set)
#     my_set.add(a)
#     after = len(my_set)
#     if before == after:
#         print('Nu am adaugat numarul in set. Acesta exista deja')
#         return False
#     else:
#         print('Am adaugat numarul nou in set')
#         return True
#
# print(numere(7, setul))
# print(setul)  # verificam daca s-a si adaugat
#
# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

# LUNI = {
#     'January' : 31,
#     'February' : 28,
#     'March' : 31,
#     'April' : 30,
#     'May' : 31,
#     'June' : 30,
#     'July' : 31,
#     'August' : 31,
#     'September' : 30,
#     'October' : 31,
#     'November' : 30,
#     'Dcember' : 31
# }

# if 'August' in LUNI:
#     print(luni_zile.get('August'))
#
# def luni(luna):
#     if luna in LUNI:
#         return LUNI.get(luna)
#     else:
#         print('Introduceti o luna corecta')
#
# print(luni('September'))

#
# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#
# def calculator(x,y):
#     a = x+y
#     b = x-y
#     c = x*y
#     d = x/y
#     return a,b,c,d
#
# a, b, c, d = calculator(2,3)
#
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#

# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
# dict = {
# 0: 0,
# 1 :2,
# 2: 0,
# 3: 1,
# 4: 0,
# 5: 3,
# 6: 0,
# 7: 2,
# 8: 0,
# 9: 1
# }

# lista1 = [1, 3, 1, 5, 9, 7, 7, 5, 5,1,1,1,1,1]
# def count(lista):
#     cnt =  {
#     0: 0,
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
#     7: 0,
#     8: 0,
#     9: 0
#     }
#     for i in cnt.keys():
#         for j in lista:
#             if i == j:
#                 cnt[i] = cnt[i]+1
#     return cnt
#
# print(count(lista1))

# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
#
# def maxim(a,b,c):
#     max = None
#     if a == b and b == c:
#         max = 'Numerele sunt egale'
#     elif a >= b and a >= c:
#         max = a
#     elif b >= a and b >= c:
#         max = b
#     else:
#         max = c
#     return max
#
# print(maxim(5,7,2))   # returneaza 7
# print(maxim(7,6,2))   # returneaza 7
# print(maxim(5,6,7))   # returneaza 7
# print(maxim(4,4,4))   # returneaza Numerele sunt egale


# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
#
# def suma_num(a):
#     suma = 0
#     for i in range(0,a+1):
#         suma = suma + i
#     return suma
#
# print(suma_num(3))  # returneaza 6

# BONUS:
#
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
#
# nume = input('Nume: ')
# numele = None
# def gen_nume(nume_input):
#     exceptii_baieti =['Mihnea', 'Mircea', 'Horia', 'Horea']
#     exceptii_fete = ['Carmen', '']
#     if (nume_input[len(nume_input)-1] == 'a' or nume_input in exceptii_fete) and nume_input not in exceptii_baieti:
#         print('este nume de fata')
#         return 'este nume de fata'
#     else:
#         print('este nume de baiat')
#         return 'este nume de baiat'
#
# numele = gen_nume(nume)

#
# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# def liste(lista1, lista2):
#     lista3 = []
#     for i in lista1:
#         for j in lista2:
#             if i == j and i not in lista3:
#                 lista3.append(lista1[i])
#     return lista3
#
# print(liste(list1,list2))  # returneaza 2,3


# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
#
#
# def reducere_preturi(price,sale):
#     new_price = price - (sale / 100) * price
#     return int(new_price)
#
# pret = 200
# reducere = 20
# print(reducere_preturi(pret, reducere))


# 19. Functie care sa afiseze data si ora curenta

#from datetime import datetime
#
# def data_ora():
#
#     date_time = datetime.now()
#     dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")  # aici am schimbat formatul
#     print("Date and Time: ", dt_string)
#
# data_ora()


# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
#
# from datetime import date, datetime
#
# dt = datetime
# now = dt.now()
#
# ziua = int(input('Ziua in care te-ai nascut: '))
# luna = int(input('Luna in care te-ai nascut: '))
# anul = now.year

# if ziua < date.today().day and luna < now.month:
#     anul = anul + 1

# from datetime import date
#
# def count_days_birthday(zi, luna, an):
#     birthday = date(year=an, month=luna, day=zi)
#     days_til_birthday = (birthday - date.today()).days
#
#     print(f'Mai ai {days_til_birthday} zile pana la ziua ta')
#
# count_days_birthday(ziua, luna, anul)

# M-AM CHINUIT CEVA VREME SA FAC SA MEARGA CU DATELE INTRODUSE DE LA TASTATURA, DAR A IESIT :D

# MAI JOS E O ALTA VARIANTA CARE MERGE, DAR NU STIU CUM SA FAC SA NU-MI MAI AFISEZE SI TIMPUL

# import datetime
# def count_days(zi, luna, an):
#     dt = datetime.datetime
#     now = dt.now()
#     timeleft = dt(year = an, month = luna, day = zi) - dt(year=now.year, month=now.month, day=now.day)
#
#     print(timeleft)
#
# count_days(ziua, luna, anul)

