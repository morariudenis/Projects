# # calculator de impozit in functie de centi cubi
#
# cc = int(input('Cati centrimetri cubi'))
# impozit = None
#
# def calcul_impozit(cc_input, hybrid_input):
#     if hybrid_input == True:
#         return 10
#     else:
#         if cc_input < 1000:
#             return 70
#         elif cc_input < 2000:
#             return 160
#         else:
#             return 900
#
#
# # apelam functia
#
# impozit = calcul_impozit(cc, False)
#
# print(impozit) # cc49 = 70
#
# impozit = calcul_impozit(2400, False)
#
# print(impozit)  # = 900
#
# impozit = calcul_impozit(2400, True)
#
# print(impozit) # 10
#

# % de benzina ramasa + daca scadem sub 15%, afisam un warning
#
# benz = int(input('Benzina ramasa:'))
# benz_ramasa = None
# REZERVOR = 50
# def benzina_ramasa (benzina_input, REZERVOR):
#     procentaj_benz = benzina_input/REZERVOR * 100
#     print(procentaj_benz)
#     if procentaj_benz <= 15:
#         return 'Warning'
#
# benz_ramasa = benzina_ramasa(benz,REZERVOR)


# nume de baiat sau fata?
# intr-un return daca e baiat sau fata

nume = input('Nume: ')
numele = None
def gen_nume(nume_input):
    if nume_input[len(nume_input)-1] == 'a':
        print('este nume de fata')
        return 'este nume de fata'
    else:
        print('este nume de baiat')
        return 'este nume de baiat'

numele = gen_nume(nume)