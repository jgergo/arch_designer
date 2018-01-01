import random
import numpy
from deap import base, creator, tools, algorithms


creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", set, fitness=creator.Fitness)

# Create the item dict: item name is an int, and value is a (weight, value) tuple

NMBR_ITEMS = 100
IND_INIT_SIZE = 5
MAX_ITEM = 50
MAX_WEIGHT = 50

items={}
for i in range(NMBR_ITEMS):
    items[i] = (random.randint(1, 10), random.uniform(0, 100))

toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NMBR_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def eval_knapsack(individual):
    weight = 0.0
    value = 0.0
    for item in individual:
        weight += items[item][0]
        value += items[item][1]
    if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
        return 10000, 0
    return weight, value


def cx_set(ind1, ind2):
    """
    Apply crossover operation on input sets. The first child is the intersection of the two sets, the second child
    is the difference of the two sets.
    """
    temp = set(ind1)    # to keep the original
    ind1 &= ind2        # intersection (inplace)
    ind2 ^= temp        # symmetric difference (inplace)
    return ind1, ind2


def mut_set(individual):
    """
    Mutation that pops or adds an element
    """
    if random.random() < 0.5:
        if len(individual) > 0:
            individual.remove(random.choice(sorted(tuple(individual))))
        else:
            individual.add(random.randrange(NMBR_ITEMS))
    return individual,


toolbox.register("evaluate", eval_knapsack)
toolbox.register("mate", cx_set)
toolbox.register("mutate", mut_set)
toolbox.register("select", tools.selNSGA2)


def main():
    random.seed(40)
    NGEN = 500
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.3

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats, halloffame=hof, verbose=True)

    return pop, stats, hof


if __name__ == '__main__':
    main()