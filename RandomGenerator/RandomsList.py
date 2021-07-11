import random


def generate_randoms(start, stop, seed, count):
    random.seed(seed)
    return [random.randint(start, stop) for r in range(count)]