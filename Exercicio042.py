"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

print('-='*20)
print('ANALISADOR DE TRIANGULO...')
print('-='*20,'\033[31;33m')
t1 = float(input('Digite o primeiro segmento:'))
t2 = float(input('Digite o segundo segmento:'))
t3 = float(input('Digite o terceiro segmento:'))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos PODEM FORMAR um triangulo!')  
    if t1 == t2 == t3:
        print('É um triangulo EQUILATERO!')
    elif t1 != t2 != t3 != t1:
        print('É um triangulo ESCALENO!')
    else:
        print('É im triangulo ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triangulo!')
    