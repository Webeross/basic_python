#ENcontrar caracteres iguais dentro do Nome: digitado, Ex AR dentro de Eduardo
'''nome = input('Digite seu nome: ')
encontrar = input('Oque deseja encontrar: ')

if encontrar in nome:
        print(f'{encontrar} está em {nome}')

else:
        print(f'{encontrar} não está em {nome} ')'''

'''numero = 10
 
#Encontrar número maior que 1, 2, 3 Como a maquina le de baixo para cima, ele capta o 3, 2, 1
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')'''

#Interpolação;

nome = 'Dudu'
preco = 1999
variavel = '%s o preço de nascer em %i é estar próximo dos 24 anos' % (nome, preco) 
# %(mais a primeira letra primitiva, ex; %string e %int)


    