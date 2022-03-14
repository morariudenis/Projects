# a. Recomandat (usor)
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva
#
# b. Obligatorii (mediu)
#
# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#
# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
#
# PI = 3.14
# class cerc():
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Raza cercului este: {self.raza}')
#         print(f'Culoarea cercului este: {self.culoare}')
#
#     def aria(self):
#         self.aria = PI * self.raza**2
#         print(f'Aria cercului este: {self.aria}')
#
#     def diametru(self):
#         self.diam = self.raza*2
#         print(f'Diametrul cercului este: {self.diam}')
#
#     def circumferinta(self):
#         print(f'Circumferinta cercului este: '"{:0.2f}".format(self.diam * PI))
#
#
# cerc1 = cerc(5,'alb')
#
# cerc1.descrie_cerc()
# cerc1.aria()
# cerc1.diametru()
# cerc1.circumferinta()
# 2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
#
# class dreptunghi():
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f'Culoare cercului este: {self.culoare}')
#         print(f'Lungimea cercului este: {self.lungime}')
#         print(f'Latimea cercului este: {self.latime}')
#
#     def aria(self):
#         print(f'Aria dreptunghiului este: {self.latime * self.lungime}')
#
#     def perimetru(self):
#         print(f'Perimetrul dreptunghiului este: {2 * (self.latime + self.lungime)}')
#
#     def schimb_culoare(self, culoare_noua):
#         self.culoare = culoare_noua
#
# drept1 = dreptunghi(4,7,'roz')
#
# drept1.descrie()
# drept1.perimetru()
# drept1.aria()
# drept1.schimb_culoare('alb')
# drept1.descrie()
#
# 3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
#
# class angajat():
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Nume: {self.nume}')
#         print(f'Preume: {self.prenume}')
#         print(f'Salariu: {self.salariu}')
#
#     def nume_complet(self):
#         print(f'Numele complet: {self.nume} {self.prenume}' )
#
#     def salariu_lunar(self):
#         print(f'Salariul lunar este: {self.salariu}')
#
#     def salariu_anual(self):
#         print(f'Salariul anual este: {self.salariu * 12}')
#
#     def marire_salariu(self, procent):
#         self.procent = procent
#         self.salariu = int((self.procent / 100 * self.salariu) + self.salariu)
#         print(f'Salariul lunar dupa marire este: {self.salariu}')
#
# angajat1 = angajat('Morariu', 'Denis', 5000)
#
# angajat1.descrie()
# angajat1.nume_complet()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu(50)
# angajat1.descrie()   # am apelat ca sa vad ca s-a schimbat salariul initial in cel de dupa marire
# angajat1.salariu_anual()  # si salariul anual e schimbat


# 4.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#

# from datetime import date
#
# import TableIt
# SERIA = 'KJKJDF'
# class factura():
#
#     SERIA = 'KJKJDF'
#     mylist = None
#
#     def __init__(self, nume, nume_produs, cantitate, pret_buc):
#         self.nume = nume
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     def genereaza_factura(self, numar):
#         SERIA = 'KJKJDF'    # nu stiu unde ar fi trebuit sa pun SERIA in interiorul clasei incat sa o vada cand o apelez, e ok daca pun o variabila
#         self.numar = numar
#         print(f'Factura seria: {SERIA} numar: {self.numar}')
#         today = date.today()
#         d1 = today.strftime("%d/%m/%Y")
#         print("Data:", d1)
#         self.mylist = [
#             [ 'Nume', "Cantitate", 'Pret bucata', 'Total'],
#             [self.nume_produs, self.cantitate, self.pret_buc, (self.cantitate * self.pret_buc)],
#             ]
#         TableIt.printTable(self.mylist, useFieldNames=True)
#
#  # Aici am gasit libraria asta cu tabele, arata mai dragut. A trebuit sa ma joc putin cu ea incat sa mearga totul bine, dar a iesit.
#  # Tu daca nu ai instalata libraria nu stiu daca poti sa dai RUN si sa vezi ce vad eu.
#
# factura1 = factura('Morariu', 'Telefon', 20, 100 )
# factura1.schimba_pretul(150)
# factura1.genereaza_factura(23232)
# factura1.schimba_cantitatea(200)
# factura1.genereaza_factura(23232)
# factura1.schimba_nume_produs('Tableta')
# factura1.genereaza_factura(23232)

#
# 5.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
#
#
# class cont():
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban}, suma de {self.sold} lei')
#
#     def debitare_suma(self,suma):
#         self.suma = suma
#         self.sold = self.sold + self.suma
#         print(f'Contul a fost debitat cu {self.suma} lei') # am adaugat printuri ca sa arate mai frumos in consola
#
#     def creditare_suma(self,suma):
#         self.suma = suma
#         if self.suma > self.sold:
#             print('Soldul este insuficient pentru creditare')
#         else:
#             self.sold = self.sold - self.suma
#             print(f'Contul a fost creditat cu {self.suma} lei')
#
# cont1 = cont('CNT3831039172343', 'POPESCU ION', 5000)
#
# cont1.afisare_sold()
# print(' ')
# cont1.creditare_suma(500)
# cont1.afisare_sold()
# print(' ')
# cont1.debitare_suma(1000)
# cont1.afisare_sold()

#
#
#
# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
#
# 6.
# Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0
#
# class masina():
#
#     marca = 'Audi'
#     culoare = 'gri'
#     model = None
#     viteza_actuala = 0
#     inmatriculata = False
#     culori_disponibile = {'gri', 'alb', 'rosu', 'negru', 'verde', 'maro'}
#
#
#     def __init__(self,model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f'Model masina: {self.marca}')
#         print(f'Culoarea masinii: {self.culoare}')
#         print(f'Modelul masinii: {self.model}')
#         if self.inmatriculata == False:
#             print('Masina nu este inmatriculata')
#         else:
#             print('Masina este inmatriculata')
#         print(f'Viteza masinii este: {self.viteza_actuala}')
#
#     def inmatriculare(self):
#         if self.inmatriculata == False:
#             self.inmatriculata = True
#         else:
#             print('Masina este deja inmatriculata')
#
#     def vopseste(self, culoare):
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#         else:
#             print(f'Culoare {culoare} nu este disponibila')
#
#
#     def accelerare(self,viteza):
#         if viteza <= self.viteza_maxima and viteza > 0:
#             self.viteza_actuala = viteza
#         elif viteza > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#         else:
#             print('Viteza nu poate fi negativa')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#
# masina1 = masina('A4', 260)
#
# masina1.descrie()
# print(" ")       # am pus print ca sa se inteleaga ceva in consola
# masina1.inmatriculare()
# masina1.descrie()
# print(" ")
# masina1.vopseste('portocaliu')
# masina1.descrie()
# print(" ")
# masina1.vopseste('negru')
# masina1.descrie()
# print(" ")
# masina1.accelerare(300)
# masina1.descrie()
# print(" ")
# masina1.franeaza()
# masina1.descrie()

#
# 7. Clasa TodoList
#
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
#
# Metode:
# adauga_task() - se va adauga in dict
# finalizeaza_task() - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
#

# class todolist():
#
#     todo = {
#
#
#     }
#
#     def adauga_task(self):
#         self.todo['masina'] = 'Spala masina'
#         self.todo['dentist'] = 'Programare dentist ora 12'
#         self.todo['curs'] = 'Finalizeaza tema de la curs'
#
#     def finalizeaza_task(self,task):
#         self.task = task.casefold()
#
#         if self.task in self.todo:
#             self.todo.pop(self.task)
#             print(f'Task-ul {self.task} a fost finalizat')
#         else:
#             print(f'Task-ul {self.task} nu este in lista')  # aici voiam sa il fac mai ok cumva, am mai adaugat chestii
#
#     def afiseaza_todo_list(self):
#         print(f'To do list: {self.todo.keys()}')
#
#     def afiseaza_todo(self):  # aici am adaugat metoda ca sa vad cum arata tot dict-ul cu taskuri si detalii
#         for key, value in self.todo.items():  # am facut asa ca sa arate mai frumos
#             print(key, ' : ', value)
#
#     def afiseaza_detalii_suplimentare(self, new_task):
#         self.new_task = new_task
#         if self.new_task not in self.todo:
#             print(f'Task-ul {self.new_task} nu este in lista, ati dori sa il adaugati?')
#             self.raspuns = input('Scrieti raspunsul (da/nu): ')
#             if self.raspuns == 'nu':
#                 print('La revedere')
#             else:
#                 self.detalii = input('Scrieti detalii pentru noul task: ')
#                 self.todo[new_task] = self.detalii
#
# todo1 = todolist()
#
# todo1.afiseaza_todo_list()
# todo1.adauga_task()
# todo1.afiseaza_todo()
# print(' ')
# todo1.afiseaza_todo_list()
# print(' ')
# todo1.finalizeaza_task('casa')
# print(' ')
# todo1.finalizeaza_task('masina')
# todo1.afiseaza_todo()
# print(' ')
# todo1.afiseaza_todo_list()
# print(' ')
# todo1.afiseaza_detalii_suplimentare('caine')
# todo1.afiseaza_todo_list()
# print(' ')
# todo1.afiseaza_todo()
#
