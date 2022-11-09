"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para
 o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""


num = int(input('Digite um numero inteiro:'))
print('O numero digitado foi:', num)
print('Digite [1] para converter o numero em BINARIO.')
print('Digite [2] para converter o numero em HEXADECIMAL.')
print('Digite [3] para converter o numero em OCTAL.')
opção = int(input('Digite a opção desejada:'))

if opção == 1:
    print('O numero {} convertido em BINARIO é igual {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O numero {} convertido em OCTAL é igual {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('O numero convertido em HEXADECIMAL é igual {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida... Tente novamente!')

