import random


def generate_randoms(start, stop, seed, count, duplicate=False):
    random.seed(seed)
    return [random.uniform(start, stop) for i in range(count)]
