# acceleram pana mai avem benzina
#
# benzina_ramasa = 5
# consum = 0.5
# while benzina_ramasa > 0:
#     print('vruum vruum')
#     benzina_ramasa = benzina_ramasa - consum
#     if benzina_ramasa <= 3:
#         print('bec rosu')
#     print(f'mai ai {benzina_ramasa} benzina litri ramasa')
# else:
#     print('stop nu mai ai beznina')
#
# # avand o lista de numere reale afisati doar nr pozitive
#
# numere = [-1, -4, 0, 2, 6, 7, 12 ]
# numere2 = []
# for numar in numere:
#     if numar > 0:
#         print(numar)
#         numere2.append(numar)
# print(numere2)

# for numar in numere:
#     if numar <= 0:
#         continue
#     print(numar)

# accesam valori cu for each din dict.

note_elevi = {
    'Marius' : 10,
    'Ana' : 9,
    'Andy' : 5,
    'Hanna' : 8
}
for elev, nota in note_elevi.items():
    print(elev, nota)
    if nota > 7:
        print(f'{elev} a luat nota {nota}')

# cati au luat 7?
counter = 0
for elev, nota in note_elevi.items():
    if nota == 7:
        counter += 1
print(f'{counter} elevi au luat nota 7')


