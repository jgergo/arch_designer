import random
from deap import base, creator, tools


IND_SIZE = 5

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)



def mutation(ind):
    mutant = toolbox.clone(ind)
    ind2, = tools.mutGaussian(mutant, mu=0.0, sigma=0.2, indpb=0.2)     # the comma is very important
    del mutant.fitness.values
    return ind2


def crossover(ind1, ind2):
    child1, child2 = [toolbox.clone(ind) for ind in (ind1, ind2)]
    tools.cxBlend(child1, child2, 2)
    del child1.fitness.values
    del child2.fitness.values
    return child1, child2


def selection(population):
    selected = tools.selBest(population, 2)
    return selected


def evaluate(individual):
    a = sum(individual)
    b = len(individual)
    return a, 1./b


def main():
    ind1 = toolbox.individual()
    ind2 = mutation(ind1)
    print(ind1)
    print(ind2)

    ind1.fitness.values = evaluate(ind1)
    ind2.fitness.values = evaluate(ind2)
    print(ind1.fitness)
    print(ind2.fitness)

    child1, child2 = crossover(ind1, ind2)
    child1.fitness.values = evaluate(child1)
    child2.fitness.values = evaluate(child2)
    print(child1.fitness)
    print(child2.fitness)

    selected = selection([child1, child2])
    offspring = [toolbox.clone(ind) for ind in selected]


if __name__ == '__main__':
    main()
