# cei 4 piloni ai OOP (Encapsulare, )
# 1.exceptii - prindem si tratam o exceptie
# exceptii = situatii cand codul nu poate executa instructiunile
# se foloseste sintaxa try/except

#Aici trata, toate erorile
# try: # aici punem codul despre care presupunem ca ar putea genea o exceptie
#     number = 0
#     number2 = 10/number
# except Exception as e: # aici tratam orice exceptie (slvam mesajul ei in variabila e)
#     print(f'Error: {e}.')

# aici tratam orice index error, aici prindem specific
# try:
#     lista = [1, 2, 3]
#     lista[6]
# except IndexError as e:
#     print(e)

# aici fortezi o exceptie
# raise IndexError('Limita eroriloe din clasa este 30.')

# ex: cand verifici ceva ce nu exista in pagina, atunci primesti eroare
# try:
#     # verific ca selenium imi da aceasta eroare
# except Exception as e:
#     assert True
#     print('Ne asteptam la asta.')
# -------------------------------------------------------------------------------------------
# cei 4 piloni ai OOP

# 1.inheritance = cand o clasa copil mosteneste o clasa parinte si are acces la toate atributele si metodele clasei parinte
# o clasa copil poate mosteni de la doua sau mai multe clase parinte
# __atribut = 1 => asa se scund atribute, merge si la metode

# 2.polymorphism = cand exista doua functii cu acleasi numa, dar au comportament diferit
# ex: len

# 3. Abstraction
# o METODA ABSTRACTA = definita la nivelul clasei abstrae si care nu are corp/logica si trebuie implementata la nivelul clasei copil ce urmeaza sa o mosteneasca
# o metoda abstracta = are doar nume, urmeaza sa fie definita candva ( nu are corp)
# o CLASA ABSTRACTA contine metode fara corp, dar si metode cu logica definita
# exista clase abstracte care contin metode abstracte
# INTERFATA = o clasa ce contine metode abstracte ce urmeaza sa fie implementate ulterior de alte clase
# o clasa abstracta = metode abstracte, dar si metode proprii (normale) care tine de clasa
# ABSTRACTIZARE (in programre) = sa expunem utulizatoruui minimul necesar de info, doar ce este de intereul lui
# DECORATOR arata asa: @abstractmethod

# encapsulation = ascunderea atributelor  pentru nu aglomera
# putem folosi pe atributele ascunse urmatoarele functiii: getter, setter, deleter (get, set, delete) -> le folosim cand accesam atribute ascunse
# putem sa folosim doar una dintre ele sau toate

# decoratorul @property ne ajuta sa folosim getter, setter, deleter intr-un mod Pythonic.
# ex
# class CarPy:
#     def __init__(self, color):
#         self.__color = color
#     @property # culoarea este o proprietate a clasei CarPy
#     def color(self):
#         return self.__color
# propr se comporta ca niste atribute definite in clasa, dar sunt contruite pe baza metodelor: getter, setter, deleter

