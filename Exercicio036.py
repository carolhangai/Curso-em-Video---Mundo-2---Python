"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""


vlcasa = float(input('Qual valor do imovel R$?'))
sal = float(input('Qual salario do comprador R$?'))
anos = int(input('Em quantos anos vai pagar o emprestimo?'))
prest = vlcasa /(anos * 12)
prestmax = sal * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} reais em {} anos'.format(vlcasa,anos))
print('A prestação mensal será no valor de R${:.2f} reais'.format(prest))

if prest <= prestmax:
    print('Emprestimo concedido!')
    
else:
    print('Emprestimo negado!Valor acima de 30% do salario.') 
