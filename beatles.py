# etapa 1
beatles = []

print("Etapa 1:", beatles)


# etapa 2
beatles.append ('John Lennon, Paul McCartney, George Harrison' )

print("Etapa 2:", beatles)


# etapa 3

num_novos_membros = int(input("Quantos novos membros você deseja adicionar? "))
for _ in range(num_novos_membros):
    novo_membro = input("Digite o nome do novo membro da banda: ")
    beatles.append(novo_membro)


# etapa 4

del beatles[3:5]

# passo 5
beatles.insert (-1, 'Ringo Starr')

print("Membros da banda:")
for membro in beatles:
    print(membro)


# testando o tamanho da lista

print("o fabuloso", len(beatles))