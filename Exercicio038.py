"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro número:'))
print('O primeiro número digitado foi {}'.format(num1))
print('O segundo número digitado foi {}'.format(num2))
if num1 > num2:
    print('O PRIMEIRO valor digitado foi {},e é MAIOR que o segundo valor {}.'.format(num1, num2))
elif num1 < num2:
    print('O SEGUNDO valor digitado foi {},e é MAIOR2 que o primeiro valor {}'.format(num2, num1))
else:
    print('O primeiro valor digitado foi {},e é IGUAL ao segundo valor {}'.format(num1,num2))

    
