import os

lista=[]

while True:
    print('selecione uma opção')
    opcao=input('[i]inserir  [a]apagar  [l]listar').upper()

    if opcao=='I':
        os.system('cls')
        valor=input('valor: ')
        lista.append(valor)


    elif opcao=='A':
        indice_str=input('escolha um indice para apagar')

        try:
            indice_int=int(indice_str)
            del lista[indice_int]
        except :
            print("não foi possivel apagar o produto")
    elif opcao=='L':
        os.system('cls')

        if len(lista)==0:
            print('não há nada na lista')
        
        for i, valor in enumerate(lista):
            print(i, valor)


    else:
        print('escolha I, A ou L')