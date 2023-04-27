nome = input('Qual o seu nome? ')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso /altura ** 2

linha_1 = f'{nome} tem {altura:.2f}m de altura'
linha_2 = f'{peso:.0f}KG e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1, linha_2, linha_3)






