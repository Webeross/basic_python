a = 'a'
b = 'b'
c = 1.1
#Dentro da {} colocar a ordem, sempre começa com 0. Parametro nomeado, dar o nome a chamada ex; invés de 0, 1 = nome3
string = 'a={1} b={0} a={1} b={0} c={nome3:.2f}'
formato = string.format(a, b, nome3=c)


print(formato)