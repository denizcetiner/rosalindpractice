from functools import reduce
import matplotlib.pyplot as plt

factorials = {0: 1, 1: 1}


def factorial(n: int):
    if n in factorials:
        return factorials[n]
    else:
        factorials[n] = n * factorial(n-1)
        return factorials[n]


def combination(n: int, k: int):
    top = factorial(n)
    bottom = reduce(lambda x, y: x*y, [factorial(k), factorial(n-k)])
    return top / bottom


def get_binomial_dist(probability=0.25, n=4):
    binomial_dist = []
    for i in range(n+1):
        coeff = combination(n, i)
        success = pow(probability, i)
        failure = pow(1-probability, n-i)
        binomial_dist.append(coeff * success * failure)
    return binomial_dist


def draw_plot(dist=[]):
    plt.plot(dist)


def run(input="2 1"):
    params = input.split()
    generations = int(params[0])
    at_least = int(params[1])
    probability = 0.5 * 0.5 # when paired with an heterozygous, you always get 0.5 probability for heterozygous children.
    binomial_dist = get_binomial_dist(probability, pow(2, generations))
    draw_plot(binomial_dist)
    result = 0
    for i in range(at_least, len(binomial_dist)):
        result += binomial_dist[i]
    result = float("{0:.3f}".format(round(result,3)))
    print(result)
    return result
