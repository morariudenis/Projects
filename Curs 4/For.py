# for
# este un ciclu controlat, ii sun unde sa incepara si pana unde sa mearga si pace-ul
# range
# de unde incepem, daca nu punem default e 0
# pana unde? dar va fi penultima
# pasul, optional
for i in range(20, 40, 2): # i = 0
    print(i)
else:
    print(f'la iesirea din for i are valoarea {i}')

for i in range(101, 0, -2):  # i = 0
    print(i)
else:
    print(f'la iesirea din for i are valoarea {i}')

# sa folosim for ca sa parcurgem lista
# facem noi replace; inlocuim alb cu fuxia

culori = ['albastru', 'alb', 'verde', 'rosu' 'alb']
for i in range(len(culori)):
    print(f'culoarea mea preferata este {culori[i]}')
    if culori[i] == 'alb':   # daca culoarea este alb vreau sa ...
        culori[i] = 'fuxia'
    print(culori)
# print(f'culori actualizate {culori}')

# forici sau for each
# trecem prin toate elementele
# nu afisam functia
for culoare in culori: # pentru fiecare culoare din culori
    if culoare == 'fuxia':
        index = culori.index('fuxia') # aflam indexul unde este functia
        culori[index] = 'magenta'  # suprascriem lista in acel index

print(f'Culori actualzate v2 {culori}')

# un alt caz in care folosim for each

note = [3, 5, 8, 10]
s = 0
# sa aflu media aritmetica a clasei

for nota in note:
    s = s + nota
else:
    media = s / len(note)
    print(f'media clasei este {s}')


