# Otimizacao - Programacao Linear
from scipy.optimize import linprog
c = [-5, -2]
A = [[1, 2]]
b = [9]
x0_bounds = (0, 3)
x1_bounds = (0, 4)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
###### valores otimos da funcao ####################
print('####### otimizacao ######')
print(' ')
print('valores ótimos de x:',res.x)
print('----------------------------')
print('valor ótimo da função:', -res.fun)


