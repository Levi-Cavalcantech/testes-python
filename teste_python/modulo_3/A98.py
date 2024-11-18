cont_regressiva=10
CPF=input('digite o CPF: ')
CPF_tratado=CPF.replace('.','').replace('-','')
calculo=0

for digito_1 in CPF_tratado[:9]:
    calculo+= int(digito_1)*cont_regressiva
    cont_regressiva-=1

digito=(calculo*10)%11

primeiro_numero = digito if digito<=9 else 0

if primeiro_numero == int(CPF_tratado[9]):
    cont_regressiva=11
    calculo=0

    for digito_2 in CPF_tratado[:10]:
        calculo+= int(digito_2)*cont_regressiva
        cont_regressiva-=1

    digito=(calculo*10)%11

    segundo_numero = digito if digito<=9 else 0
else:
    print("o CPF é inválido")

if segundo_numero == int(CPF_tratado[10]):
    print('seja bem vindo')
   




    