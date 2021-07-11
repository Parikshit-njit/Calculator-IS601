import random


def generate_randoms(start, stop, seed, count):
    random.seed(seed)
    return random.sample(range(start, stop), count)