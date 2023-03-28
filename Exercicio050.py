"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
contador = 0
for c in range(1,7):
    num = int(input("Digite um numero:"))
    if num %2==0:
        soma = soma + num
        contador = contador + 1
print('Voce informou {} numeros pares e a soma entre eles é de {}'.format(contador,soma))




