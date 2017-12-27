import random
from deap import base, creator, tools

"""Tool decoration is a very powerful feature that helps to control very precise things during an evolution without 
changing anything in the algorithm or operators. A decorator is a wrapper that is called instead of a function. It is 
asked to make some initialization and termination work before and after the actual function is called. For example, 
in the case of a constrained domain, one can apply a decorator to the mutation and crossover in order to keep any 
individual from being out-of-bound. The following defines a decorator that checks if any attribute in the list is 
out-of-bound and clips it if this is the case. The decorator is defined using three functions in order to receive the 
min and max arguments. Whenever the mutation or crossover is called, bounds will be checked on the resulting 
individuals. """


def check_bounds(min, max):
    def decorator(func):
        def wrapper(*args, **kargs):
            offspring = func(*args, **kargs)
            for child in offspring:
                for i in range(len(child)):
                    if child[i] > max:
                        child[i] = max
                    elif child[i] < min:
                        child[i] = min
            return offspring

        return wrapper

    return decorator


MIN, MAX = 0, 10

toolbox = base.Toolbox()

toolbox.register("mate", tools.cxBlend, alpha=0.2)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=2)

toolbox.decorate("mate", check_bounds(MIN, MAX))
toolbox.decorate("mutate", check_bounds(MIN, MAX))
