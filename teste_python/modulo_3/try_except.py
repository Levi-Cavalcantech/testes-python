numero_str=input('digite um numero: ')
#try except faz um teste no try e ele executa o codigo ate o momento do erro, onde pula pro except, caso contrario, faz o codigo todo
try:
    print(f'STR: {numero_str}')
    numero_float=float(numero_str)
    print('FLOAT: ', numero_float)
    print(f"o dobro de {numero_float} e {numero_float*2}")
except:
    print('Voce nao digitou um numero')