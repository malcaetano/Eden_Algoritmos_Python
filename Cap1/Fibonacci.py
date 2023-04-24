# fibonacci
n=int(input('número de termos desejado = '))

ult=0
penul=1
i=3
while i<=n:
    soma=ult+penul
    print('termo = ',i,'fibonacci = ',soma)
    ult=penul
    penul=soma
    i=i+1

