while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite um operador: (+,-,/,*)')

    numeros_validos = None

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('um dos numeros, ou ambos esta(ao) invalido(s)')
        continue


    operador_valido = '+-*/'

    if (numero_1 and numero_2) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('digite um numero valido')
        continue

    if operador not in operador_valido:
        print('digite um operador valido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float}={numero_1_float+numero_2_float}')
    elif operador == '-':
        print(f'{numero_1_float}-{numero_2_float}={numero_1_float-numero_2_float}')
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float}={numero_1_float/numero_2_float}')
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float}={numero_1_float*numero_2_float}')

        
    sair= input("Você deseja sair ? [s]im: ").lower().startswith('s')

    if sair is True:
        break
print('ate mais')

