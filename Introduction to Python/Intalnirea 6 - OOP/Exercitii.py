# class Nerfgun:
#     # atribute/fields
#     culori_posibile = {'alb', 'negru', 'rosu'}
#     culoare = None
#     model = None
#     gloante = 0
#     piedica_pusa = True
#
#     # constructor
#
#     def __init__(self, model, culoare):
#         self.model = model
#         if culoare in self.culori_posibile:
#             self.culoare = culoare
#         else:
#             print(f'La initializarea obiectului {model} culoarea este invalida')
#
#     # metode
#
#     def descrie(self):
#         print(f'Modelul este {self.model}')
#         print(f'Culoarea este {self.culoare}')
#         print(f'Numar de gloante este {self.gloante}')
#         print(f'Piedica este {self.piedica_pusa}')
#
#     def scoate_piedica(self):
#         self.piedica_pusa = False
#         print('Ai scos piedica')
#
#     def trage(self):
#         if self.piedica_pusa == False and self.gloante > 0:
#             self.gloante = self.gloante - 1
#             print('Pac Pac')
#         else:
#             print('Nu ai gloante, boss')
#
#     def incarca(self, gloante):
#         if gloante > 10:
#             self.gloante = 10
#         elif gloante <= 0:
#             print('Man, pune-le cu plus')
#         else:
#             self.gloante = gloante
#
#     def pune_piedica(self):
#         self.piedica_pusa = True
# obiecte
#
# nerf1 = Nerfgun('Glock', 'alb')
# nerf2 = Nerfgun('Deagle', 'roz')
# nerf1.descrie()
# nerf2.descrie()
# nerf2.culoare = 'albastru'
# nerf1.scoate_piedica()
# nerf1.trage()
# nerf1.incarca(11)
# nerf1.descrie()
# nerf1.trage()
# nerf1.trage()
# nerf1.descrie()
# nerf1.pune_piedica()
# nerf1.trage()
# nerf1.descrie()
# nerf2.scoate_piedica()
# nerf2.incarca(1)
# nerf2.trage()
# nerf2.trage()
# nerf2.descrie()

import random

class Caine:

    def __init__(self, rasa,nume,culoare):
        self.rasa = rasa
        self.nume = nume
        self.culoare = culoare
        self.varsta = 1

    # metode
    def ani_cainesti(self):
        return self.varsta * 7
    def descrie(self):
        print(f'Nume: {self.nume}')
        print(f'Varsta: {self.ani_cainesti()}')
        print(f'Culoare: {self.culoare}')

    def la_multi_ani(self):
        self.varsta += 1

    def latra(self):
        n = random.randint(1,3)
        print(f'{self.nume}:')
        print('Ham!' * n)

grivei = Caine('golden', 'Grivei', 'alb')
azorel = Caine('doberman', 'Azorel', 'negru')

grivei.descrie()
azorel.descrie()
azorel.la_multi_ani()
azorel.descrie()
azorel.nume = 'Zdreanta'
azorel.descrie()

# amandoua variabile se vor referi la acelasi caine
zdreanta = azorel
zdreanta.la_multi_ani()
zdreanta.latra()
zdreanta.latra()
zdreanta.latra()
zdreanta.la_multi_ani()
zdreanta.descrie()
azorel.descrie()
azorel.nume = 'BUBI'
zdreanta.nume = 'puck'
azorel.descrie()
zdreanta.descrie()