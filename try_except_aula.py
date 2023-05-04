"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Digite um numero: ')

try:
    print('STRING', numero)
    soma_int = int(numero)
    print('INT', soma_int)
    print(f'O dobro de {numero} é {soma_int *2}' )

except:
    print('Isso não é um número')


'''
numero = input('Digite um numero: ')
print(numero.isdigit())

if numero.isdigit():
    soma_int = int(numero)
    print(f'O dobro de {numero} é {soma_int *2}' )
else:
    print('O valor digitado não é um número')
'''