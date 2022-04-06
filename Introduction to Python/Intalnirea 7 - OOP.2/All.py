# Exceptii

# se trateaza prin try except

# lista = [1, 2, 3]
# lista[6]

try: # in try punem codul despre care presupunem ca ar putea genera o exceptie
    number = 20
    number2 = number/0
except Exception as e: # in except tratam orice exceptie ( salvam mesajul ei in variabila e)
    print(f'Error: {e}')
# number = 20
# number2 = number/0
print('ajung aici')

try: # in try punem codul 'periculos'
    lista = [1,2,3]
    lista[6]
except IndexError as e: # tratam IndexError exception
    print(e)

# fortam o exceptie
raise IndexError('Limita elevilor din clasa este 30')
# mai mult in caz de IF cand apare ceva sa fortez o eroare

# try: # in try punem codul despre care presupunem ca ar putea genera o exceptie
#    # verific ca selenium imi da aceasta eroare
# except Exception as e: # in except tratam orice exceptie ( salvam mesajul ei in variabila e)
#     assert True
#     print('Ne asteptam la asta')