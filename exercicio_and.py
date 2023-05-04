"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


hora = input('Que horas são: ')

try:
    hora = int(hora)

    if hora >=18 and hora <= 23:
        print('Boa noite')

    elif hora >=12 and hora <= 17:
        print('Boa tarde')

    elif hora >= 0 and hora <= 11:
        print('Bom dia')

    else:
        print('Hora inválida')
         
except:
    print('Apenas números inteiros')




