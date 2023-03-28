""" Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

num=int(input("Digite um numero para ver a tabuada:"))
for c in range (0,11):
    mult= c*num
    print(num, "X", c ,"=",mult)


"""método Guanabara
num = int(input("Digite um numero para ver a tabuada:"))
for c in range(0,11):
    print('{} x {:2} = {}'.format(num,c,num*c))"""
 