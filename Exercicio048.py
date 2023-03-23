""" Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0#p/ somar os nº multiplos
quant = 0#contador p/ calcular qtde de nº
for num in range (1, 501, 2):#(2)pula de dois em dois, trazendo apenas nº impares.
    if (num %3 == 0):# %3 == 0: resta da divisão por três igual a zero. 
        quant = quant + 1
        print('São multiplos de tres:',num)
        soma = soma + num
print('A QUANTIDADE de números multiplo de três é: {}'.format(quant))
print('A SOMA de todos os nº multiplos de três é: {}'.format(soma))
