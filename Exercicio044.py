"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros"""
#{:^50} para centralizar a frase.

print('-='*40)
print('{:^60}'.format('LOJAS COMPRE MAIS'))
print('-='*40)

compras = float(input('Qual valor das compras? R$'))
print('O valor total de suas compras é de R${} reais.'.format(compras))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais''')
opcao = int(input('Selecione forma de pagamento:'))
print('Forma de pagamento {}'.format(opcao))

if opcao == 1:
    total = compras - (compras *10/100)
    desconto = (compras *10/100)
elif opcao == 2:
    total = compras - (compras *5/100)
    desconto = (compras *5/100)
elif opcao == 3:
    total = compras
    parcela = total / 2
    desconto = 0
    print('Sua compra parcelada em 2x será de R${:.2f} reais cada parcela SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = compras + (compras * 20/100)
    desconto = 0
    total_parc = int(input('Quantas parcelas?'))
    parcela = total / total_parc
    juros = (compras * 20/100)
    print('Sua compra será parcelada em {:.2f}x e cada parcela será de R${:.2f} reais COM JUROS.'.format(total_parc,parcela))
    print('Total de JUROS R${} reais'.format(juros))
else:
    compras = 0
    print('OPÇÃO DE PAGAMENTO INVÁLIDA! TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} reais vai custar R${:.2f} reais ao final.'.format(compras,total))
print('Seu desconto foi de R${:.2f} reais'.format(desconto))




   