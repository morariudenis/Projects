# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
#
from abc import ABC, abstractmethod

PI = 3.14
class FormaGeometrica(ABC):  # abstract class contains abstract methods


    @abstractmethod  # decorator pentru metoda abstracta
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi.')

# INHERITANCE
class Patrat(FormaGeometrica): # Clasa Patrat - mosteneste FormaGeometrica

    def __init__(self, latura): # constructor pt latura
        self.__latura = latura

# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        self.__latura = latura

    def delete_latura(self):
        self.__latura = None

# Implementati metoda ceruta de interfata
    def aria(self):
        a = self.__latura * self.__latura
       # print(f'Aria patratului este de {a} cm².')

class Cerc(FormaGeometrica):  # Clasa Cerc - mosteneste FormaGeometrica

    def __init__(self, raza):  # constructor pt raza
        self.__raza = raza  # raza este proprietate privata

# Implementati getter, setter, deleter pt raza
    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def delete_raza(self):
        self.__raza = None


# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte

    def aria(self):
        a = int(2 * PI * self.__raza * self.__raza)

# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    def descrie(self):
        print('Eu nu am colturi')
#
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
l1 = Patrat(5)
print(f'Latura patraului este {l1.get_latura()} cm.')

l1.set_latura(10)
print(f'Am setat noua latura a patratului de {l1.get_latura()} cm.')

print(f'Aria patratului este de {l1.aria()} cm².')

l1.delete_latura()
print(f'Apare "None" daca latura a fost stearsa: {l1.get_latura()}')
print('')
# Creati un obiect de tip Cerc si jucati-va cu metodele lui
cerc1 = Cerc(2)
print(f'Raza cercului este {cerc1.get_raza()} cm.')

cerc1.set_raza(6)
print(f'Noua raza a cercului este {cerc1.get_raza()} cm.')

print(f'Aria patratului este de {cerc1.aria()} cm².')

cerc1.delete_raza()
print(f'Apare "None" daca raza a fost stearsa: {cerc1.get_raza()}.')


# 3. Actualizati proiectul pe github facand un push la noul cod
# In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
#
#
#