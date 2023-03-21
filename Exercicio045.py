"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""


from random import randint
from time import sleep

objetos = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''Suas opções:)
[0] Pedra
[1] Papel
[2] Tesoura''')

continuar_jogo = "sim"
while (continuar_jogo=="sim"):

    jogador =int(input('Qual sua jogada?'))
    if jogador >=3:#se escolher opção errada, sai do jogo.
        print('Opção INVÁLIDA! TENTE NOVAMENTE.')
        exit()

    print('JO.....')
    sleep(0.5)
    print('KEN......')
    sleep(0.5)
    print('PÔÔÔ!!!')
    print('-='*13)
    print('O PC jogou {}'.format(objetos[pc]))
    print('Jogador jogou {}'.format(objetos[jogador]))
    print('-='*13)

    if pc == 0: #PC jogou pedra
        if jogador == 0:
            print('Empatou!')
        elif jogador == 1:
            print('Jogador venceu!')
        elif jogador ==2:
            print('O Pc venceu!')


    elif pc == 1: #PC jogou papel
        if jogador == 0:
            print('O pc venceu!') 
        elif jogador == 1:
            print('Empatou!')
        elif jogador ==2:
            print('O jogador venceu!')


    elif pc == 2: #PC jogou tesoura
        if jogador == 0:
            print('O jogador venceu!')    
        elif jogador == 1:
            print('O Pc venceu!')
        elif jogador ==2:
            print('Empatou!')
    continuar_jogo = input("Quer jogar novamente? sim ou não?").strip().lower()
print("Até a próxima!")

