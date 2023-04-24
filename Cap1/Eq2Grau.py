import math as m

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

delta=b**2 - 4*a*c

if delta>0:
    x1=(-b+m.sqrt(delta))/(2*a)
    x2=(-b-m.sqrt(delta))/(2*a)
    print('x1 = ',x1,'  x2 = ',x2)
elif delta==0:
    x1=-b/(2*a)    
    print('duas raízes reais e iguais a x = ',x1)
else:
    print('não existem raízes reais')



    

