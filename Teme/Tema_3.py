# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)
#
# 1.
# Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]   # metoda 1
# note_muzicale.reverse()        # metoda 2
# print(note_muzicale)
# # 2.
# # De cate ori apare ‘do’?
# print(note_muzicale.count('do'))

# 3.
# Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
# Afisati lista ordonata astfel [0,1,2,3,4,5,6]
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
#
# l3 = l1.__add__(l2)
# print(l3)
# l4 = l1 + l2
#print(l4)
# l4 = sorted(l4)
#print(l4)

# 4.
# Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
# print(l4)
# l4.remove(0)
# print(l4)
# l4.pop(0)
# print(l4)
#
# 5.
# Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala
# if len(l4) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')    #  aici imi da ca lista nu este goala
# #
# # 6.
# # Folositi o functie care sa stearga lista de la ex3
#
# l4.clear()    # am golit lista
#
# # 7.
# # Copy paste la ex 5. Verificati inca o data.
# # Acum ar trebui sa se afiseze ca lista e goala
# if len(l4) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')   # aici imi da ca lista este goala
#
#
# 8.
# Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())

#
# 9.
# Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

# print(f'Ana a luat nota {dict1.get("Ana")}, Gigel a luat nota {dict1.get("Gigel")} si Dorel a luat nota {dict1.get("Dorel")}')

# 10.
# Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

# dict1['Dorel'] = 6
# print(dict1)

# 11.
# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi
#
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt
#
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')  # observam ca nu merge pentru ca set-urile au valori unice si nu putem adauga dublura
# print(zile_sapt)

# 13.
# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt

# if weekend.issubset(zile_sapt) == True:
#     print(' Weekend este un subset al zilelor din sapt')
# else:
#     print('Weekend nu este un subset al zilelor din sapt')  # imi da ca este un subset al zilelor saptamanii

# 14.
# Afisati diferentele dintre aceste 2 seturi

# print(zile_sapt.difference(weekend))
# diferenta = zile_sapt - weekend  # weekend fiiund un subset putem doar sa il scoatem si ne da diferenta
# print(diferenta)
#
# 15.
# Afisati intersectia elementelor din aceste 2 seturi

#print(zile_sapt.intersection(weekend))

#
# c. Optionale (may need google)
# 16.
# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori

jucatori = ['Mane', 'Salah', 'Firmino', 'Virgil', 'Thiago']

# Schimbari_efectuate = va jucati voi cu valori diferite

schimbari_efectuate = 1

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari

x1 = 'Mane'
x2 = 'Salah'
x3 = 'Thiago'   # aici am declarat variabilele asa ca sa imi fie mai usor sa ma joc cu ele
y1 = 'Diaz'
y2 = 'Jota'
y3 = 'Fabinho'

if schimbari_efectuate == 3:
    print('Nu mai puteti face schimbari')
elif jucatori.__contains__(x1) == True and schimbari_efectuate > 0 and schimbari_efectuate <=3:
    jucatori.remove(x1)
    jucatori.append(y1)
    print(f'A iesit {x1} si va intra {y1}, mai aveti {2 - schimbari_efectuate} schimbari')
else:
    print(f'Nu se poate efectua schimbarea pentru ca {x1} nu este in teren. Mai aveti {3 - schimbari_efectuate} schimbari')

# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori
#
# Google search hint
# “how to check if item is in list python”

