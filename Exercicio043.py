"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""


peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = (peso) / (altura * altura)
print('Seu peso é {}kg, sua altura é {}cm e seu IMC é {:.2f}'.format(peso,altura,imc))
if imc < 18.5:
    print('Voce esta ABAIXO do peso recomendado!')
elif imc > 18.5 and imc < 25:
    print('Parabens, voce esta na faixa de peso IDEAL!') 
elif imc >25 and imc <30:
    print('Voce esta com SOBREPESO!')
elif imc >30 and imc < 40:
    print('Voce esta OBESO!')
else:
    print('Esta em OBESIDADE MÓRBIDA!')