# Otimizacao - Programacao Linear
from scipy.optimize import linprog
c = [-1, 4]
A = [[-3, 1],[1,2]]
b = [6,4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
###### valores otimos da funcao ####################
print('####### otimizacao ######')
print(' ')
print('valores ótimos de x:',res.x)
print('----------------------------')
print('valor ótimo da função:', -res.fun)


