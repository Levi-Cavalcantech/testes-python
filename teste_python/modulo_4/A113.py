def mult(*args):
    resul=1
    for numeros in args:
        resul*=numeros
    return resul

def imparpar(x):
    if x%2==0:
        resul="par"
    else:
        resul="impar"
    return resul

resultado=mult(1,2,3,4,5)
ip= imparpar(resultado)

print(f'{resultado} é {ip}')