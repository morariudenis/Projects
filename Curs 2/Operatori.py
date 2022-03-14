# operatori de atribuire
x = 3
x =+ 7
print(x) # la fel ca si x = x + 10

# operatori aritmetici
print(4+6)
print(10 % 3)

# op de comparare

print(3 != 3)  # false, 3 nu e diferit de 3
print(3 == 3)  # da e egal
print(3 < 3)  # false nu e mai mic

# op logici - and, or, not
print(3>0 and 5>0)
# true and true =>
print(-3 > 0 and 5 > 0)
# false and true => false
print(3 > 0 or -5 > 0)
# true or false => true
print(-3 > 0 or -5 > 0)
# false and false => false
print(not(-3 > 0 or -5 > 0))  # concluzia e flase dar o intorc => true
# putem complica cat vrem noi
print(-3 > 0 or 3 > 0 and 5 > 0)
# false or (true and true) => true
print( -3 > 0 and 3 > 0 or 5 > 0)
# false or (true and false) => false
print(-3 > 0 or 3 > 0 and not(-5 > 0))
# false or (true and true) => true

# user - str -> true
# AND
# password - str -> true
# AND
# bifa -> true
# AND
# age > 18 - true
# OR
# user is admin = fal


# if

NOTA_DE_TRECERE_EXAMEN = 4.5  # constanta, semnalam cu litere mari sa avem grija sa nu se suprascrie
NOTA_DE_TRECERE_PURTARE = 7

if 7 >= NOTA_DE_TRECERE_EXAMEN and 9 >= NOTA_DE_TRECERE_PURTARE:
    print('Am trecut')

# if else
nota_examen = 10
nota_purtare = 10
if 7 >= NOTA_DE_TRECERE_EXAMEN and 9 >= NOTA_DE_TRECERE_PURTARE:
    print('Am trecut clasa')
    if nota_examen == 10 and nota_purtare == 10:
        print('premiul 1')
else:  # nu are conditie, pentru ca e ce a mai ramas
    print('Nu am trecut clasa')

# if else if ... else

# robotel telefonic

# optiunea = int(input('alege o optiune'))
# if optiunea == 0:
#     print('meniu anterior')
# elif optiunea == 1:
#     print('ati ales ro')
# elif optiunea == 2:
#     print('ati ales eng')
# else:
#     print('nu am gasit')
#
#
#
optiunea = int(input('alege limba, pt 1 e ro, pt 2 e eng'))
if optiunea == 1:
    print('ati ales ro')
    op2 = int(input('pers fiz 1, pers jur 2'))
    if op2 == 1:
        print('ati ales fiz')
    elif op2 == 2:
        print('ati ales jur')
    else:
        print('nu ati ales bine')
elif optiunea == 2:
    print('ati ales ro')
elif optiunea == 3:
    print('meniul anterior')
else:
    print('nu ati ales corect')


