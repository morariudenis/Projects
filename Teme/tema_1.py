# '''
# 1.Display the sum of 5 + 10, using two variables: x and y.
import math

x=5
y=10
print(x+y)
#
# 2. Creați cȃte o variabilă de tipul: string, int și float, după cum urmează:
# Variabila de tip int va reține valoarea 20.
# Variabila de tip float va reține valoarea 10.
# Variabila de tip string reține valoarea "python".
#
# x= 20
# y= 10.4
# z='python'

# 3. Utilizȃnd funcția type, determinați tipul următoarelor variabile:
# restanta = 0
# print(type(restanta))
#
# notaFinala = 10.0
# print(type(notaFinala))
#
# laborator = "Introducere in informatica"
# print(type(laborator))
# #
# 4. Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
# stanga, este tot acel cuvânt.(folositi assert pt verificare)
# cuvant = 'ana'
# assert cuvant == cuvant[::-1]
# #
# 5. Remove first n characters from a string (n il cititi de la tatatura)
# "Ana are mere" daca n=3 va afisa " are mere"
# x= input('Scrieti o propozitie: ')
# n= int(input('Stergem primele cate caractere? '))
# print(x[n::])

#
# 5.reads two numbers and multiplies them together and print out their product
# a= int(input('a='))
# b= int(input('b='))
# p= a * b
# print('Produsul lor este: ', p )
# print(f'Produs={a*b}')
# #
# 6.Check if the first and last number of a string  is the same stringul il cititi de la tastatura
# x= input('Scrieti un cuvant:')
# first_char = x[0]
# last_char = x[-1]
# assert first_char == last_char
# if first_char == last_char:
#     print('prima si ultima litera sunt aceleasi')
# else:
#     print('prima si ultima litera sunt aceleasi')
#
# 7. Write a program to find how many times substring "Emma" appears in the given string.
# str_x = "Emma is good developer. Emma is a writer"
# print(f'Emma apare de: {str_x.count("Emma")} ori')

#
# 8. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# pt "eu merg la mare" sa imi afiseze "eure"
# string = input('Scrieit o prop:')
# pr2 = string[:2]
# ul2 = string[len(string)-2:]
# print(pr2+ul2)

#
# 9. Write a Python program to calculate the length of a string.
# pt "eu merg la mare" ->15
# string = input('Scrieit o prop:')
# print(f'Propozitia are {len(string)} caracatere')

#
# 10. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
# string = str(input('Scrieit un cuvant:'))
# first_char = string[0]
# cuv_nou=string[1:]
# cuv_nou=cuv_nou.replace(first_char, '$')
# print(first_char+cuv_nou)

#
# 11. Utilizand tipurile de print pe care vi le-am aratat:
# afisati in consola I have 1000 dollars so I can buy 3 footballs for 450.00 dollars.
# totalMoney = 1000
# quantity = 3
# price = 450
# print(f'I have {totalMoney} dollars so I can buy {quantity} footballs for {price} dollars')
# #
# 12.Build a program to calculate the followings using the input from the user for a, b, c or r
import math
a= float(input('a='))
b= float(input('b='))
c= float(input('c='))
r= float(input('r='))
#
p=float((a+b+c)/2)
atr=math.sqrt(p*(p-a)*(p-b)*(p-c))
atr2 = "{:.2f}".format(atr)

print(f'The area of the triangle is {atr2}')

# • triangle area using input
# • rectangle area and perimeter
# • circle area
#
# 13. Which of the following are valid ways to specify the string literal foo'bar in Python:
# • 'foo\'bar'
# • """foo'bar"""
# • "foo'bar"
# • 'foo''bar'
# • 'foo'bar'
#
# 14.Password checker script
# Define a username getting input from the console
# Define a password getting input from the console
# Display the following message 'The password for user Paul is
# ********* is 9 characters long)

# username = input('user: ')
# password = input('password: ')
# hidden_password = '*' * len(password)
# print(f' The passwordd for user {username} is {hidden_password} and is {len(password)} characters long')
#
# de cautat pe net:
# 15.Write a program to take three names as input from a user in the single input() function call.
# x, y, z = input('Scrie 3 nume').split()
# print(x, y, z)

# 16. Display float number with 2 decimal places
# x= 3.534535434
# x = '{:.2f}'.format(x)
# print(x)

# '''