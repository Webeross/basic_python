nome = input('Qual seu nome: ')
idade = input('QUal sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrário é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço')

    else:
        print('Seu nome não contém espaço')
    
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, há campos vazios')

    


