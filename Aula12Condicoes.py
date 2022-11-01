#Estrutura condicional aninhada
nome = str(input('Qual é seu nome?')).capitalize()
if nome =='Carolina':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Joao' or nome== 'Paulo' or nome== 'Jose' or nome== 'Maria':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Carol Cecilia Sophia Clara Larissa':
    print('Que belo nome!')
#else é opcional, se nao for nenhumas das opcoes acima, vai ser essa ultima.
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia,{}!'.format(nome))   