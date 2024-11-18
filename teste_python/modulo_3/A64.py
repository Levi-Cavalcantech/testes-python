nome=input('qual o seu nome ? ')
tamanho=len(nome)
nome_espec='*'
contador=0
while contador <tamanho:
    nome_espec+=nome[contador]+'*'
    contador+=1
print(nome_espec)