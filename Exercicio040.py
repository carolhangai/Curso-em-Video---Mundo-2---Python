"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO;
– Média entre 5.0 e 6.9: RECUPERAÇÃO;
– Média 7.0 ou superior: APROVADO."""

n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
print('A primeira nota do aluno foi: {}, a segunda nota foi: {}'.format(n1,n2))
media = float(n1 + n2)/2
if media >= 7:
    print('Sua nota média é:', media)
    print('Aluno APROVADO! Parabéns!!!')
elif media >= 5 and media < 7:
    print('Sua nota média é:', media)
    print('O aluno esta em RECUPERAÇAO!')
else:
    print('Sua média é:', media)
    print('Aluno esta REPROVADO!') 
