import random

bibioteca_de_palavras = ['perfume', 'cadeira', 'mesa', 'computador', 'livro']
n_palavra_sortida = random.randint(0, len(bibioteca_de_palavras) - 1)
palavra_escolhida = bibioteca_de_palavras[n_palavra_sortida]
numero_tentativas = 0
palavra_secreta = ['*'] * len(palavra_escolhida)  # Usando uma lista para permitir modificações

while True:
    print('=-'*20)
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra_escolhida:
        for c in range(len(palavra_escolhida)):
            if letra_digitada == palavra_escolhida[c]:
                palavra_secreta[c] = letra_digitada  # Modifica a lista
    print('A palavra secreta é: ', end="") 

    for cc in range (len(palavra_escolhida)):
        print( palavra_secreta[cc], end="")
    print('')

    numero_tentativas += 1
    if '*' not in palavra_secreta:
        print('=-'*20)
        break

print("Parabens, você venceu O JOGO ")
print(f"você venceu em {numero_tentativas} tentativas")
print("=-"*20)