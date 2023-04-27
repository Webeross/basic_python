# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    nome = input('Qual o seu nome? ')
    peso = float(input('Qual o seu peso? '))
    altura = float(input('Qual a sua altura? '))
    imc = peso /altura ** 2

    linha_1 = f'{nome} tem {altura:.2f}m de altura'
    linha_2 = f'{peso:.0f}KG e seu imc é'
    linha_3 = f'{imc:.2f}'
    print(linha_1, linha_2, linha_3)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')