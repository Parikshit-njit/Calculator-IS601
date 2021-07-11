import random


def generate_randoms(start, stop, seed, count, duplicate):
    random.seed(seed)
    if duplicate:
        return [random.choice(range(start, stop)) for r in range(count)]
    else:
        return [random.randint(start, stop) for r in range(count)]
