def criar_multiplicacao(multiplicador):
    def operacao(numero):
        return numero * multiplicador
    return operacao

numero_de_entrada=int(input("digite um numero: "))

duplicar= criar_multiplicacao(2)
triplicar= criar_multiplicacao(3)
quadruplicar= criar_multiplicacao(4)

print(f'seu valor duplicado é {duplicar(numero_de_entrada)}')
print(f'seu valor triplicado é {triplicar(numero_de_entrada)}')
print(f'seu valor quadruplicado é {quadruplicar(numero_de_entrada)}')