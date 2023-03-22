"""   
"c" quer dizer contagem, mas pode usar qualquer coisa.
 (0,10) vai printar Olá mundo de zero a nove.
 (1,10) vai printar Olá mundo um a nove.
 ATENÇÃO: VAI IGNORAR O ÚLTIMO.

for c in range (0,10):
    print('Olá mundo!')
print('FIM!')"""


"""
vai printar o "c"
for c in range (0,10):
    print(c)
print('FIM!')
"""

""" 
(-1) vai printar decrescente de dez a zero.
for c in range (10,0,-1):
    print(c)
print('FIM!')
"""


"""
2) vai printar pulando de dois em dois
for c in range (0,20,2):
    print(c)
print('FIM!')
"""

"""
vai printar de zero até o numero digitado -1. (acrescente n+1 para printar até o numero digitado).
n = int(input('Digite um numero:'))
for c in range (0, n):
    print(c)
print('Fim!')
"""

""""
Mostra o inicio, fim e quantos pulos.
i = int(input('Inicio da contagem:'))
f = int(input('Fim da contagem:'))
p = int(input('Quantos passos/pulo:'))
for c in range (i, f+1, p):
    print(c)
print('Fim!')
"""

"""
printa a quantidade indicada (0,3)
for c in range (0,3):
    n=int(input("Digite um valor:"))
print('Fim!')
"""

soma = 0
for c in range (0,3):
    numero=int(input("Digite um valor:"))
    soma = soma + numero
print('A soma de todos o valores digitados é de {}.'.format(soma))
print('Fim!')
