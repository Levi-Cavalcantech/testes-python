nome= str(input('Qual seu nome? '))
idade= int(input('Qual sua idade? '))
if nome and idade:
    print(f'Seu nome e {nome} e sua idade e {idade}')
    print('seu nome invertido é ', nome[::-1])

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome nao tem espaços')

    print('a primeira letra do seu nome e ', nome[0].upper())
    print('a ultima letra do seu nome e ', nome[-1].upper())
else:
    print('Preencha os dados corretamente')
    