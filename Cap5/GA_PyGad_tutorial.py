#Algoritmo Genetico - PyGad
# Instalacao: >> pip install pygad
###################################################
# resolvendo a funcao
# y = f(w1:w6)=w1x1+w2x2+...+w6x6
###################################################
import pygad
import numpy as np

function_inputs = [4,-2,3.5,5]
desired_output = 44

def fitness(solution,solution_idx):
    output=np.sum(solution*function_inputs)
    fit = 1.0 / np.abs(output - desired_output)
    return fit


################ parametros do algoritmo ###################
num_generations = 50
num_parents_mating = 4

fitness_function = fitness
sol_per_pop = 8
num_genes = len(function_inputs)
init_range_low = -2
init_range_high = 5
parent_selection_type = "sss"
keep_parents = 1
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10
##########################################################

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       mutation_percent_genes=mutation_percent_genes)
ga_instance.run()

print("Generation : ", ga_instance.generations_completed)
print("Fitness of the best solution :", ga_instance.best_solution()[1])
ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))