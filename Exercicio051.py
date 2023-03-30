""": Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""


"""correção professor Guanabara
num = int(input('Digite o primeiro termo:'))
raz = int(input('Digite a razao:'))
decimo = num + (10-1)*raz
for c in range(num,decimo + raz,raz):
    print('{}'.format(c), end=' - ')
print('FIM!')"""

print('='*45)
print('Os dez termos de uma Progressão Aritmética')
print('='*45)
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = primeiro + 10 * razao
for c in range(primeiro, decimo, razao):
    print(c, end=' - ')# end='-' é para permanecer na mesma linha.
print('FIM!')

  
  


