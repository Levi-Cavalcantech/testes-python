import os

lista_de_compras=[]
item_inserido=[]
while True:
    os.system('cls')
    for indice in range(len(lista_de_compras)):
        print(indice, lista_de_compras[indice])
    print('selecione um opção:')
    print('[i]inserir  [a]apagar  [l]listar')
    escolha=input('opção: ').upper()

    if escolha == 'I':
        os.system('cls')
        item_inserido+= input('insira um item: ')
        continue

    elif escolha =="A":
        os.system('cls')
        if lista_de_compras== []:
            continue
        else:
            for indice in len(lista_de_compras):
                print(indice, lista_de_compras[indice])
            apagar=input('escolha o indice do produto que você quer apagar')
            lista_de_compras.pop(apagar)
            continue
    elif escolha =='L':
        lista_de_compras.append(item_inserido)
        item_inserido=[]
        continue
    else:
        continue

