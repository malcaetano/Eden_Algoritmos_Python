#simples operacao com numeros imaginarios
a=0.2
b=-0.5
z=a+1j*b
print('+++++++++++ sucessivos produtos de z = a +bi++++')
for i in range(3):
    z=z**2
    print('%5.4f %5.4fi'% (z.real,z.imag))

print('++++++++++++++++++++++++++++++++++++++++++++')   

 