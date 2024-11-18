import random


nove_digitos=''
for c in range(0,9):
    nove_digitos+=str(random.randint(0,9))

cont_regressiva=10
calculo=0

for digito_1 in nove_digitos[:9]:
    calculo+= int(digito_1)*cont_regressiva
    cont_regressiva-=1

digito=(calculo*10)%11

primeiro_numero = digito if digito<=9 else 0
nove_digitos+=str(primeiro_numero)
if primeiro_numero == int(nove_digitos[9]):
    cont_regressiva=11
    calculo=0

    for digito_2 in nove_digitos[:10]:
        calculo+= int(digito_2)*cont_regressiva
        cont_regressiva-=1

    digito=(calculo*10)%11

    segundo_numero = digito if digito<=9 else 0
    nove_digitos+=str(segundo_numero)
else:
    print("o CPF é inválido")

if segundo_numero == int(nove_digitos[10]):
    print(f'{nove_digitos} é válido')
   




    