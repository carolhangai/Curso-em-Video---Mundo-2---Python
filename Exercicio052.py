"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input("Digite um número: "))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        contador = contador + 1
        print('Divisivel por:',c)

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é PRIMO!")
else:
    print("O número NÃO é primo!")