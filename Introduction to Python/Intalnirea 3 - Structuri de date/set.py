# am valori unice , nu conteaza altceva
# cand aleg culorile unei masini nu vreau sa am aceiasi culoare de 2 ori

vocale = {'a', 'e', 'i', 'o', 'u'}
abc = {'a', 'b', 'c'}
# sa adaugam un duplicat
before = len(vocale)
vocale.add('a')
after = len(vocale)
if before == after:
    print('ai adaugat un duplicat')
print(vocale)
print(abc.issubset(vocale)) # daca abc e inclus in vocale
print(abc.intersection(vocale)) # print care e in ambele
print(abc.union(vocale)) # print ambele fara dubluri

litera = 'b'
if litera in vocale:   # asa cautam daca ceva e in altceva
    print('Litera e vocala')
else:
    print('Nu e vocala')
