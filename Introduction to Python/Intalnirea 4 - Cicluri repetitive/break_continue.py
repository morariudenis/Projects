# break -> nu se mai executa codul scris dupa
# intrerupe iteratia, iese automat din for

for i in range(100):
    if i == 7:
        break  # iesim din for
    print(i)
print('se continua cu codul din fisier')

# cand se foloseste break?
# cand caut acul in carul cu fan
# cand caut o valoare intr-o lista si dupa ce am gasit, am satisfacut cerinta


# continue da skip la iteratia actuala, trimite codul inapoi la inceput de for/while
# il folosim cand vrem sa excludem anumite valori din lista

for i in range(0, 20):
    if i == 3 or i == 12:
        continue
    print(i)

i = 0
while i <=30:
    print(i)
    if i == 7 or i == 17:
        i = i + 1
        continue # trimite codul la inceput de while
    print('nu vom vedea acest cod pt 7 si 17')
    i = i + 1
