# cheie -> valoare
# se folosesc {} dar se adauga : intre cheie si valoare
# sunt mutabile si ordonate
# cheile sunt unice, sunt ca niste porecle pt indexuri

# dict - structura cheie : valoare
# NU PUTEM AVEA CHEI DUPLICATE
capitale = {
    'Romania' : 'Bucuresti',
    'Ungaria' : 'Budapesta',
    'Italia'  : 'Roma',
    'Bulgaria': 'Sofia'
}
# putem sa accesam date?
print(capitale.get('Romania'))
print(capitale['Romania'])
# suprascriere/update
capitale['Romania'] = 'Cluj'
# adaugare
capitale['Ucraina'] = 'Kiev'
print(capitale)

# stergere
capitale.pop('Romania')
print(capitale)

# editare cu updaate
capitale2 = {'Romania' : 'Buc', 'Rusia' : 'Moscova', 'Italia' : 'Milan'}
capitale.update(capitale2)
# edit cu update 2
capitale.update({'Romania' : 'Stp', 'Rusia' : 'Moscova'})
print(capitale)


