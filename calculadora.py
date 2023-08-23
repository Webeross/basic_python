numero1 = float(input('Digite o primeiro número: '))

numero2 = float(input('Digite o segundo número: '))

operacao = input('Digite a operação (+, -, *, /): ')

if operacao == '+':
    print('Sua conta é: ', numero1 + numero2)

elif operacao == '-':
    print('Sua conta é', numero1 - numero2 )

elif operacao == '*':
    print('Sua conta é ', numero1 * numero2)

else:
    print('Sua conta é', numero1 / numero2 )
    
