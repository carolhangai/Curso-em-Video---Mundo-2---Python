""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

hoje = date.today().year
nasce = int(input( 'Qual seu ano de nascimento?'))
idade = hoje - nasce
print('Quem nasceu em {} tem {} anos em {}.'.format(nasce,idade,hoje))
if idade < 18 :
    saldo = 18 - idade
    print('Ainda não esta em idade para se alistar!Faltam {} anos para o alistamento.'.format(saldo))
    ano_alist = hoje + saldo
    print('Seu alistamento será no ano de {}.'.format(ano_alist))
elif idade == 18:
    print('Voce tem {} anos, deve se alistar!'.format(idade))
else:   
    saldo = idade - 18
    print('Já passou da idade de se alistar!Voce deveria ter se alistado há {} anos.'.format(saldo))
    ano_alist = hoje - saldo
    print('Seu alistamento foi no ano de {}.'. format(ano_alist))
