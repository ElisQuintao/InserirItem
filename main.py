# inserir um item na lista - create
cobras = ['sucuri', 'piton', 'Mamba Negra', 'Naja']

# ebxibir a lista
for cobra in cobras:
    print(cobra)

#usuario informa o nome da nova cobra
nova_cobra = input('\nInforme o nome da nova cobra: ')

#inserir nova cobra na lista
cobras.append(nova_cobra) # o append insere um novo item no final da lista, dentro do parentese coloca a variavel do novo item.
print('\n')

# exibir a lista
for cobra in cobras:
    print(cobra) # ira exibir a lista como o novo item porem não salva esse novo item.

# ordernar a lista
cobras.sort()

print('\n')

#exibir a lista ordenada
for cobra in cobras:
    print(cobra)

